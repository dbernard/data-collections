import csv
import praw


def today():
    r = praw.Reddit(user_agent='Test script by /u/roadhause')
    top = list(r.get_subreddit('all').get_top_from_day(limit=100))
    for post in top:
        print post


if __name__ == '__main__':
    today()

