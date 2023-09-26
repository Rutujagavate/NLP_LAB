'''
Assignment_no :- 02
Name :- Rutuja Pandurang Gavate
Roll_No :- 21
Batch :- B2
Assignment_Title :- Text pre-processing using Natural Language processing, 
                    Perform Bag of Words and TF-IDF using Gensim library
'''
import gensim
from gensim import corpora

#-----------------------BOW-----------------------------------------------

text1 = ["""Gensim is a free open-source Python library for representing documents as semantic vectors,
           as efficiently and painlessly as possible. Gensim is designed 
           to process raw, unstructured digital texts using unsupervised machine learning algorithms."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

#O/P
'''
{'Gensim': 0, 'Python': 1, 'a': 2, 'algorithms.': 3, 'and': 4, 'as': 5, 'designed': 6, 'digital': 7, 'documents': 8, 'efficiently': 9, 'for': 10, 'free': 11, 'is': 12, 'learning': 13, 'library': 14, 'machine': 15, 'open-source': 16, 'painlessly': 17, 'possible.': 18, 'process': 19, 'raw,': 20, 'representing': 21, 'semantic': 22, 'texts': 23, 'to': 24, 'unstructured': 25, 'unsupervised': 26, 'using': 27, 'vectors,': 28}
Bag of Words :  [[(0, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 3), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 2), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1)]]
'''
#-----------------------TF-IDF------------------------------------------


text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])
