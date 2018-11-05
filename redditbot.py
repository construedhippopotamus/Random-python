# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 19:35:48 2018

@author: Pizzagirl

reddit bot

followed instructions here:
    http://pythonforengineers.com/build-a-reddit-bot-part-1/
    https://praw.readthedocs.io/en/latest/getting_started/installation.html
    
lib location:
C:\ProgramData\Anaconda2\envs\py36\Lib\site-packages\praw
    
"""

#  30 requests/min MAX
import praw
import re
import os

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

os.chdir(r'C:\python36scripts')

file = r'C:\python36scripts\redditposts.txt'

posts_replied_to = []

with open(file, "a") as f:
    try:
        posts_replied_to = f.read()
    except:
        pass
    else:
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        print("type", type(posts_replied_to))
        

#get top 5 submissions
for submission in subreddit.hot(limit=5):
    print(submission.title, "\n")#, submission.selftext, submission.score, "\n")
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("i'm stuck in a pit of pythons")
            print("Bot replying to : ", submission.title)
    
            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("redditposts.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
    
