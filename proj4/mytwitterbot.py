# mytwitterbot.py
# IAE 101, Fall 2024
# Project 04 - Building a Twitterbot
# Name: Vincent Yang
# netid: viyyang
# Student ID: XXXXXXXXX

import os
import time
import random
import tweepy
import simple_twit
from PIL import Image, ImageFilter
import dotenv

dotenv.load_dotenv()

# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# API Key, also known as Consumer Key
API_KEY = os.getenv("API_KEY")

# API Key Secret, also known as Consumer Secret
API_KEY_SECRET = os.getenv("API_KEY_SECRET")

# Project 04 Exercises

# Exercise 1 - Get and print 3 tweets from your home timeline
# For each tweet, print:
#   the tweet ID,
#   the author ID,
#   the tweet creation date, and
#   the tweet text


def exercise1(client):
    timeline: tweepy.Response = simple_twit.get_home_timeline(
        client, 3)

    tweet: tweepy.Tweet
    for tweet in timeline.data:
        print(f"""tweet ID: {tweet.id}
author ID: {tweet.author_id}
tweet creation date: {tweet.created_at}
tweet text: {tweet.text}""")


# Exercise 2 - Get and print 3 tweets from another user
# For each tweet, print:
#   the tweet ID,
#   the author ID,
#   the tweet creation date, and
#   the tweet text


def exercise2(client):
    tweets = simple_twit.get_users_tweets(client, "Minecraft")

    tweet: tweepy.Tweet
    for tweet in tweets.data[:3]:
        print(f"""tweet ID: {tweet.id}
author ID: {tweet.author_id}
tweet creation date: {tweet.created_at}
tweet text: {tweet.text}""")

# Exercise 3 - Post 1 tweet to your timeline.


def exercise3(client):
    simple_twit.send_tweet(client, f"Wow. I love Twitter! {time.time()}")


# Exercise 4 - Post 1 media tweet to your timeline.
def exercise4(client):
    simple_twit.send_media_tweet(
        client, "dg pic :3", f"assets/{random.choice(os.listdir("assets"))}")


# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(client):
    def new_image():
        im = Image.open(f"assets/{random.choice(os.listdir("assets"))}")
        width, height = im.size
        mat = (random.random() * 2, 0, 0, 0,
               0, random.random() * 2, 0, 0,
               0, 0, random.random() * 2, 0)
        im = im.convert("RGB", mat)
        q = int(random.random() * 8) + 1
        b = int(random.random() * 32)
        im = im.filter(ImageFilter.GaussianBlur(b))
        im = im.quantize(1 << q).convert("RGB")
        r = int(random.random() * 6)
        im = im.resize((width // (1 << r), height // (1 << r)),
                       Image.Resampling.NEAREST)
        im = im.resize((width, height), Image.Resampling.NEAREST)
        name = f"bot/{int(time.time())}.jpg"
        im.save(name)
        return name
    simple_twit.send_media_tweet(client, "", new_image())


if __name__ == "__main__":
    # This call to simple_twit.create_client will create the Tweepy Client
    # object that Tweepy needs in order to make authenticated requests to
    # Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "client" holding this Tweepy Client object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    print()

    try:
        client = simple_twit.create_client(API_KEY, API_KEY_SECRET)
    except Exception as e:
        print("ERROR:", e)

    print(client)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.\
    # print("EXERCISE 1")
    # exercise1(client)

    # print("EXERCISE 2")
    # exercise2(client)

    # print("EXERCISE 3")
    # exercise3(client)

    # print("EXERCISE 4")
    # exercise4(client)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(client)
