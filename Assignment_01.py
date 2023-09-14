'''
Assignment_no :- 01
Name :- Rutuja Pandurang Gavate
Roll_No :- 21
Batch :- B2
Assignment_Title :- Natural Language processing, process like Tokenization,Stop Words,
                    Lemmatization of sentences by using Spacy library.
'''


#-------------------------Tokenization-------------------------------

import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Hello, my name is rutuja pandurang gavate"
    "I currently pursuing the B.tech in IT"
    "I am from the shevgaon"
    "Thank you"
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)

'''
Hello 0
, 5
my 7
name 10
is 15
rutuja 18
pandurang 25
gavateI 35
currently 43
pursuing 53
the 62
B.tech 66
in 73
ITI 76
am 80
from 83
the 88
shevgaonThank 92
you 106

'''

#--------------------Stop Words--------------------------

import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

'''
should
whose
more
them
their
also
and
further
besides
beforehand

'''
#-----------------------------------------------------

custom_about_text = (
     "Hello, my name is rutuja pandurang gavate"
    "I currently pursuing the B.tech in IT"
    "I am from the shevgaon"
    "Thank you"
   
)
nlp = spacy.load("en_core_web_sm")
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])


'''
[Hello, ,, rutuja, pandurang, gavateI, currently, pursuing, B.tech, ITI, shevgaonThank]

'''

#---------Lemmatization-------------------------

import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Hello, my name is rutuja pandurang gavate"
    "I currently pursuing the B.tech in IT"
    "I am from the shevgaon"
    "Thank you"
   
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

'''
               Hello : hello
                  is : be
            pursuing : pursue
                  am : be
       shevgaonThank : shevgaonthank

'''