'''
Assignment_no :- 01
Name :- Rutuja Pandurang Gavate
Roll_No :- 21
Batch :- B2
Assignment_Title :- Text pre-processing using Natural Language processing, 
                    Perform Tokenization,Stop Words,Lemmatization and Part of Speech 
                    using Spacy library tagging use any sample text.
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

#--------------Part-of-Speech Tagging--------------------

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
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )


'''
TOKEN: Hello
=====
TAG: UH         POS: INTJ
EXPLANATION: interjection

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: my
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: name
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: rutuja
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: pandurang
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: gavateI
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: currently
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: pursuing
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: B.tech
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: in
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: ITI
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: am
=====
TAG: VBP        POS: AUX
EXPLANATION: verb, non-3rd person singular present

TOKEN: from
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: shevgaonThank
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

'''
