#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, codecs, csv

kanawords = {}
tweets = {}

for row in codecs.open("dictionary.txt","r","shift_jis"):
    row0 = row.rstrip().split("\t")
    kanawords[row0[0]] = row0[1]
    print row0[0], row0[1]

f = open("abeshinzo.txt.chasen","w+")
for row in f:
    row = row.rstrip()
    if row == "EOS":
        pass
    else:
        for word in kanawords[0]:
            if word in row:
                row = word
            else:
                pass

