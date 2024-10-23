#Jeremias BDLA
#Lexical simplifier 1

#import for cleaner method
from cleanr import cleen
#word embedding import
import gensim
from nltk.data import find

reg = 'And from the first floor to the sixth they sought and conjectured and delved in their brains.'

news = cleen(reg)
cops = reg


#***COMPLEX WORD IDENTIFICATION***
#function that returns complex words in a list based on word length
def identify(list):
	words = []
	for word in list:
		if len(word)>=7:
			words.append(word)

	return words
cwrd = identify(news)

#***SUBSTITUTION GENERATION/RANKING***
def w_embed(c_list):
#Saving pretrained word2vec/word embedding model
	word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
	model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

	w2 = []
	for c in c_list:
		w1 = []
		if c in model.key_to_index:
			shrt = len(c)
			sim = model.most_similar(positive=[c], topn = 7)
			for w, v in sim:
				if len(w)<=shrt:
					w1.append(c)#save old term
					w1.append(w)#else save new term
		elif c not in model.key_to_index:
			w1.append(c)
		w2.append(w1)

	return w2

we = w_embed(cwrd)
#print(we)

#***SUBSTITUTION RANK/REPLACEMENT***
def substitute(synlist, copyl):
	
	for synl in synlist:
		sam = synl[0]
		if len(synl) == 0:
			st0 = copyl
			old = st0.replace(sam, sam)
			copyl = old
			l = old
		else:
			#ideentifing shortest string in given synl list
			mini = min(synl, key=len)
			#replace
			st1 = copyl
			n = st1.replace(sam, mini)
			copyl = n
			l = n
	return l
print(substitute(we, cops))
