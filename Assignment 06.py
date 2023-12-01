"""
Assignment No: 06
Name: Gavate Rutuja Pandurang
Roll: 21
Batch: B2
Practical : Implement and visualize Dependency Parsing of Textual Input using Stan- ford CoreNLP and Spacy library
"""

from sys import displayhook
#from tkinter.tix import DisplayStyle
from tkinter.ttk import Style as DisplayStyle
from spacy import displacy
import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = "My school starts at 8:00.We always eat dinner together.They take the bus to work. He doesn't like vegetables."
piano_doc = nlp(piano_text)
for token in piano_doc:
print(
f"""
TOKEN: {token.text}=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }""")
displacy.serve(piano_doc, style="dep")

