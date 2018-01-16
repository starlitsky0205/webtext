#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, codecs, csv

kanawords = {}
tweets = {}

for row in open("dictionary.txt","r"):
    row0 = row.rstrip().split("\t")
    kanawords[row0[0]] = row0[1]

f = open("abeshinzo.txt.chasen","r")
for row in f:
    row = row.rstrip()
    if row[0] == "EOS":
        pass
    else:
        for word in kanawords:
            if word in row[0]:
                row[0] = word
            else:
                pass
        f2 = open("censored.txt","a")
        f2.write(row[0])
