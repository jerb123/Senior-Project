#Jeremias Brea De Los Angeles
#Lexical simplifier 2

#import json to open dictionary file
import json

#import for cleaner method
from cleanr import cleen

#word embedding imports
import gensim
from nltk.data import find

reg = 'And from the first floor to the sixth they sought and conjectured and delved in their brains.'
s_splt = cleen(reg)
cops = reg


#To Open Dictionary file
with open('freq_dict.json', 'r') as openfile:
	jsnob = json.load(openfile)

freq = jsnob

#***COMPLEX WORD IDENTIFICATION( UPDATE )***
#function that returns complex words in a list based on word frequency in the dictionary
def identify(list):
	wrds = []

	for word in list:
		if word in freq and freq[word] < 6:
			wrds.append(word)
		elif word.lower() not in freq:
    		#print('misses', word)
			wrds.append(word)
    	#else:
    		#print('simple', word)
	return wrds


#This version of identify currently returns a list of selected complex words based on lowest frequency from the dictionary
#print(identify(s_splt))
comw = identify(s_splt)



#***SUBSTITUTION GENERATION***

#Saving pretrained word2vec model and using it generate a listed list of similar terms corresponding
#to a given listed list of terms
def w_embed(c_list):
#creating variables for the path and the activation of the word2vec model via gensim lib
	word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
	model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

#create an empty list outside loop
	w1 = []

#loop through every word in the given list of complex words
	for c in c_list:

#create an empty list within first loop
		w2 = []

#if a word from the given list can be found within the gensim model's vocab
		if c in model.key_to_index:

#create a variable that finds 10 most similar words to a given comlex word using gensim's most similar function
			sim = model.most_similar(positive=[c], topn = 10)

#for every tuple within the similar words varible
			for w, v in sim:
				w2.append(w)
		else:
			w2.append(c)
      
#append the inner loop lists to the list outside the loops
		w1.append(w2)	

#return outer loop
	return w1

#variable to pass into rank
ng = w_embed(comw)

print(w_embed(comw))



#***SUBSTITUTION RANKING**
#returns a list of terms with highest frequencies from a listed list
def rank(l_list):
#create two empty lists
	minl = []
#create a variable equal to an empty string
	maxst = ''
#for every list in the given list
	for l in l_list:
#if list length greater than
		if len(l) > 1:
			mint = 10
			for word in l:
				if len(word) < mint:
					mint = len(word)
					maxst = word		
			minl.append(maxst)
		else:
#create a new variable to equal the first index of single term lists
			same = l[0]
#append that word to the outter list
			minl.append(same)
#return list
	return minl

simp = rank(ng)
print(simp)

 

#***SUBSTITUTION REPLACEMENT***
def substitute(compl, simpl, ssplt, copst):
	dew = {}

	for k, v in zip(compl, simpl):
		dew.update({k:v})

	for t in ssplt:
		if t in dew:
			st = copst
			new = st.replace(t, dew[t])
			copst = new
	l = copst	 
	return l
  
print(substitute(comw, simp, s_splt, cops))




