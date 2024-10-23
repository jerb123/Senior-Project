#Jeremias Brea De Los Angeles
#Lexical simplifier 4
 
#import json to open dictionary file
import json

#import for cleaner method
from cleanr import cleen

#import of NLTK's own thesaurus from its corpus package
from nltk.corpus import wordnet

#word embedding imports
import gensim
from nltk.data import find

reg = 'And from the first floor to the sixth they sought and conjectured and delved in their brains.'
s_splt = cleen(reg)#using cleaner function from dict to process string!!!*****
cops = reg


#OPEN Dictionary file
with open('dict_4.json', 'r') as openfile:
	jsnob = json.load(openfile)

freq = jsnob

#***COMPLEX WORD IDENTIFICATION***
#This version of identify currently outputs a list of omplex words based on dict frequency
#function takes in list of split string
#strictly returns parameter terms as well as terms not in the dictionary
def identify(list):
	wrds = []

#for each word in given split list of terms
	for word in list:

#if the word is in the dictionary and word freq value is less than 6
		if word in freq and freq[word] < 6:#maybe reverse is true?

#append word to empty outter list
			wrds.append(word)

#else if the lower case term is not in the dictionary
		elif word.lower() not in freq:

    		#print('misses', word)

#append word to empty outter list
			wrds.append(word)

#return outter list	
	return wrds

comp_W = identify(s_splt)

print(comp_W)


#***SUBSTITUTION GENERATION***
def w_embed(c_list):
#creating variables for the path and the activation of the word2vec model via gensim lib
#Saving pretrained word2vec model
	word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
	model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

#create an empty list outside loop
	w1 = []#***maybe change name


	doop = 0

#loop through every word in the given list of complex words
	for c in c_list:

#creating a variable that saves the sets to a given word(c)
		c_set = wordnet.synsets(c)

#create an empty list within first loop
		w2 = []#***maybe change name

#if a word from the given list can be found within the gensim model's vocab
		if c in model.key_to_index:#key_to_index is the new name/func for vocab (github)

#create a variable that finds 15 most similar words to
# a given word using gensim's most similar function
			sim = model.most_similar(positive=[c], topn = 10)

#for every tuple within the similar words func varible
			for w, v in sim:

#append the word of the tuple to the list within the 1stloop
				w2.append(w)

#Thesaurus extension** if word is not in w2vmodel and is within synset(thesaurus) 
		elif c not in model.key_to_index and c_set:

#for every synset in the synsets set to a word
			for syn in c_set:

#for every word in each synset
				for lemma in syn.lemmas():

#if the word is not equivalent to given complex word
					if lemma.name() != c:

#save the word in a new string variable
						s = lemma.name()

#append the string word to an inner list
						w2.append(s)

#else if the length of a word's given synset is only 1
					elif len(syn.lemmas()) == 1:


#append the word into an inner list(w2)
						w2.append(lemma.name())#check syn.lemma() for single terms to save/append

#in the case where the given complex word is not within the w2vmodels
# vocab, or the thesaurus
		else:

#append word to an inner list, (saves terms that are too unique?)	
			w2.append(c)


#append the inner loop lists to the list outside the loops
		w1.append(w2)


#return outer loop
	return w1

#variable to pass into rank
ng = w_embed(comp_W)

	
print(ng)



#***SUBSTITUTION RANK***
#It works!!! Look at notes for psuedo
def rink(lisht):
	topw = []
	maxs = ''
	for l in lisht:
		if len(l)==1:
			am = l[0]
			topw.append(am)
		else:
			maxv = 0 #max counter integer for each single list
			for wrd in l:
				# maxv = 0 #this seems to return last term in given list***
				if wrd in freq:
					# print(wrd)
					# print(freq[wrd])
					if freq[wrd]>maxv:
						maxv = freq[wrd]
						maxs = wrd
			topw.append(maxs)
	return topw


simp_W = (rink(ng))


#**Underscore removals**
def undescr(lis):
#loop through list len of list
	for i in range(len(lis)):
#replace underscore of each word index
		lis[i] = lis[i].replace('_', ' ')
	return lis

simp_r = undescr(simp_W)

print(simp_r)

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
# print(cops)
print(substitute(comp_W, simp_r, s_splt, cops))
