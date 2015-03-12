#!/usr/bin/env python

from nltk.corpus import brown
from nltk import FreqDist, ConditionalFreqDist
fd = FreqDist()
cfd = ConditionalFreqDist()

# for each tagged sentence in the corpus, get the (token, tag) pair and update
# both count(tag) and count(tag given token)
for sentence in brown.tagged_sents():
    for (token, tag) in sentence:
        fd.inc(tag)
        cfd[token].inc(tag)

# The most frequent tag is ...
print(fd.max())

# Initialize a list to hold (numtags,word) tuple
wordbins = []

# Append each (n(unique tags for token),token) tuple to list
for token in cfd.conditions():
    wordbins.append((cfd[token].B(), token))

# Sort tuples by number of unique tags (highest first)
wordbins.sort(reverse=True)

# The token with max. no. of tags is ...
print(wordbins[0])

# masculine pronouns
male = ['he', 'his', 'him', 'himself']

# feminine pronouns
female = ['she', 'hers', 'her', 'herself']

# initialize counters
n_male, n_female = 0, 0

# total number of masculine samples
for m in male:
    n_male += cfd[m].N()

# total number of feminine samples
for f in female:
    n_female += cfd[f].N()

# calculate required ratio
print(n_male/n_female)
n_ambiguous = 0
for (ntags, token) in wordbins:
    if ntags > 1:
        n_ambiguous += 1

# number of tokens with more than a single POS tag
print(n_ambiguous)
