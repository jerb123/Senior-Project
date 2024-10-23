#External cleaner function
import nltk
#use for punctuation library
import string
from nltk.tokenize import word_tokenize

def cleen(txt):
#create an empty list
	nonums = []
#Var that tokenizes words in text file with nltk function word_tokenizer
	tokens = word_tokenize(txt)

#Removes integer values tokens list(from blog.ekbana.com)
	for t in tokens:
		if not t.isnumeric():
			nonums.append(t)

#Remove punctuation (check if its preserving apostrophies)
	nopunk = [w.lower() for w in nonums if w not in string.punctuation]

	return nopunk

#This removes punctuation from the given tokenized text and returns assigned variable
