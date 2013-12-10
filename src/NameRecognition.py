import nltk
import numpy
from nltk.corpus import treebank
from nltk.tree import *
from nltk.draw import tree

class mediaNameRecognition:
	def __init(self):
		None
		
	
	def runMediaRecognition(self, sentence):
		
		tokens = nltk.word_tokenize(sentence)
		
		tagged = nltk.pos_tag(tokens)
		pos_tags = nltk.pos_tag(tokens)
		#print nltk.ne_chunk(pos_tags, binary=True)
		grammar = "NP: {<NNP>+}"
		"""
		NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
		      {<NNP>+}                # chunk sequences of proper nouns
		"""
		cp = nltk.RegexpParser(grammar)
		tree = cp.parse(pos_tags)
		
		for subtree in tree.subtrees():
			
			if subtree.node == "NP":
				print subtree
			if "Sandler" in sentence:
				print sentence
		
		"""sentences = nltk.sent_tokenize(post) [1]
		sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
		sentences = [nltk.pos_tag(sent) for sent in sentences]
		grammar = "NP: {<DT>?<JJ>*<NN>}"
		cp = nltk.RegexpParser(grammar)
		result = cp.parse(sentences[0])
		print result"""
