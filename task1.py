#!/usr/bin/env python


# import the gutenberg collection
from nltk.corpus import gutenberg

# import FreqDist class
from nltk import FreqDist

# what corpora are in the collection ?
print(gutenberg.fileids())

# create frequency distribution object
fd = FreqDist()

# for each token in the relevant text, increment its counter
for word in gutenberg.words('austen-persuasion.txt'):
    fd[word] += 1

print(fd.N()) # total number of samples
print(fd.B()) # number of bins or unique samples

# Get a list of the top 10 words sorted by frequency
for word, count in fd.most_common(10):
    print(word, count)

# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Count each token in each text of the Gutenberg collection
fd = FreqDist()
for text in gutenberg.fileids():
    for word in gutenberg.words(text):
        fd[word] += 1

# Initialize two empty lists which will hold our ranks and frequencies
ranks = []
freqs = []

# Generate a (rank, frequency) point for each counted token and
# and append to the respective lists, Note that the iteration
# over fd is automatically sorted.
for rank, (word, _) in enumerate(fd.most_common()):
    ranks.append(rank+1)
    freqs.append(fd[word])

# Plot rank vs frequency on a log-log plot and show the plot
plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()
