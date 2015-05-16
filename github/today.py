import time
import json
import requests

today_date = time.strftime("%Y-%m-%d")

r = requests.get('https://api.github.com/search/repositories?q=created:>%s'\
                 '&sort=stars&order=desc' % today_date)

if r.ok:
    trending = json.loads(r.content)

    for item in trending['items']:
        print '%s stars: %s - %s' % (item['stargazers_count'],
                                     item['name'],
                                     item['description'])

