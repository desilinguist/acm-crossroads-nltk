#!/usr/bin/env python


from nltk.corpus import brown, stopwords
from nltk import ConditionalFreqDist
cfd = ConditionalFreqDist()

stopwords_list = stopwords.words('english')

def is_noun(tag):
    return tag.lower() in ['nn','nns','nn$','nn-tl','nn+bez',
                           'nn+hvz', 'nns$','np','np$','np+bez',
                           'nps', 'nps$','nr','np-tl','nrs','nr$']

for sentence in brown.tagged_sents():
    for (index, tagtuple) in enumerate(sentence):
        (token, tag) = tagtuple
        token = token.lower()
        if token not in stopwords_list and is_noun(tag):
            window = sentence[index+1:index+5]
            for (window_token, window_tag) in window:
                window_token = window_token.lower()
                if window_token not in stopwords_list and is_noun(window_tag):
                    cfd[token].inc(window_token)


# OK. We are done ! Let's start associating !
print('left ->', cfd['left'].max())
print('life ->', cfd['life'].max())
print('man ->', cfd['man'].max())
print('woman ->', cfd['woman'].max())
print('boy ->', cfd['boy'].max())
print('girl ->', cfd['girl'].max())
print('male ->', cfd['male'].max())
print('ball ->', cfd['ball'].max())
print('doctor ->', cfd['doctor'].max())
print('road ->', cfd['road'].max())


