'''Sentence completion solver based on word similarity'''

import nltk
import random
import gensim
import operator
import sys
import numpy as np


def solve(sentence, answers):
    model = gensim.models.Word2Vec.load('learning/models/text8_model')
    stopwords = nltk.corpus.stopwords.words('english')

    sentence_rm_stopwords = [i.strip('.').strip(',').strip().lower()
                             for i in sentence.split() if i not in stopwords]
    # print sentence_rm_stopwords
    # idx = sentence_rm_stopwords.index('-------')
    # amplitude = 2
    # min_bound = (idx - amplitude) if idx > amplitude else 0
    # max_bound = (idx - len(sentence_rm_stopwords)) if \
    #     (idx < len(sentence_rm_stopwords)) else \
    #     (len(sentence_rm_stopwords))
    # print sentence_rm_stopwords
    # sentence_rm_stopwords = sentence_rm_stopwords[min_bound: max_bound]
    keywords = [i for i in sentence_rm_stopwords if i in model]
    keyword_vectors = [model[keyword] for keyword in keywords]

    scores = {}
    for answer_key, answer in answers.iteritems():
        # print answer
        dist = 0
        scoring = []
        for keyword in keywords:
            b = False
            answer_split = answer.split('. .')
            strip_answer_split = []
            for a in answer_split:
                a = a.strip()
                strip_answer_split.append(a)
                if a not in model:
                    b = True
            if b:
                break
            scoring.append(model.n_similarity(strip_answer_split, [keyword]))
        scoring.sort()
        top_n = 5
        # print scoring[-top_n:-1]
        scores[answer_key] = (sum(scoring[-top_n:-1])/(top_n-1))
        # print "\n"

    best_choice = max(scores.iteritems(), key=operator.itemgetter(1))[0]
    # for i in answers.keys():
    #     print answers[i], scores[i]
    return best_choice