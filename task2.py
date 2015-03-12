#!/usr/bin/env python


from nltk.corpus import gutenberg
from nltk import ConditionalFreqDist
from random import choice

cfd = ConditionalFreqDist()
prev_word = None
for word in gutenberg.words('austen-persuasion.txt'):
    cfd[prev_word].inc(word)
    prev_word = word

word = 'therefore'
i = 1

# Find all words that can possibly follow the current word
# and choose one at random
while i < 20:
    print(word, end=" ")
    lwords = list(cfd[word].samples())
    follower = choice(lwords)
    word = follower
    i += 1
