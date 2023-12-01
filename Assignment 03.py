from nltk import ngrams
from nltk.util import ngrams
#unigram model
n = 1
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all
other words already in the sentence.NTK provides another function everygrams that converts a sentence
into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.' unigrams = ngrams(sentence.split(), n)
for item in unigrams:
print(item)
#bigram model
n = 2
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all
other words already in the sentence.NTK provides another function everygrams that converts a sentence
into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.' unigrams = ngrams(sentence.split(), n)
for item in unigrams:
print(item)
#trigram model
n = 3
sentence = 'While unigram model sentences will only exclude the UNK token, models will also exclude all
other words already in the sentence.NTK provides another function everygrams that converts a sentence
into unigram, bigram, trigram, and so on till the ngrams, where n is the length of the sentence. In short, this function generates ngrams for all possible values of n.' unigrams = ngrams(sentence.split(), n)
for item in unigrams:
print(item)
#using text file input
from nltk import ngrams
file = open("/home/exam/Desktop/NLP_LAB75/al.txt")
for i in file.readlines():
cumulative
