#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy

consumer_key        = 'NkIQit4MjASn108O9U5vdNVj5'
consumer_secret     = '1twiBuPOYPIEmPncOn0BvEJijW7zt1hWvVwRLGu3aRcqaai9km'
access_token        = '929360164968263680-VP55eWa2rmKWS6H7He4usToULtNvtFe'
access_token_secret = 'fhoLvv7JXTPYK3YxOOuRzyPhFppdWtR9LoMOsdpPIHELK'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# Mentionの取得
# 自分宛てのツイートを取得して表示
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.text, tweet.user.screen_name

# ツイートを送信
try:
    api.update_status(status='Hello, world!')
except tweepy.TweepError as e:

