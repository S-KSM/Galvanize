
# coding: utf-8

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

import collections
import numpy as np
import sys


def analyze_txt(a = 'pg52670.txt'):
    text = open(a).read()
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    uniquewords = set(words)
    print("Total word count: %d\nUnique words: %d\nSentences: %d" %(len(words),len(uniquewords),len(sentences)))
    print("The average number of words per line: %d" %np.round(np.mean([len(i.split(" ")) for i in sentences])))
    
if __name__ == "__main__":

    analyze_txt(sys.argv[-1])    

