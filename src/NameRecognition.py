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
				firstLeaf = subtree.leaves()[0]
				firstString = firstLeaf[0]
				
				if firstString.endswith("."):
					#check first leaf to see if a leaf of a
					#subtree begins with a string with a period
					#and the end.  This happens sometimes when a
					#PN begins a sentence, the previouse tuple gets
					#included as a PN
					subtree.pop(0)
				
				if len(subtree)>1:
					print subtree
			"""if "Sandler" in sentence:
				#print sentence
				"""
		"""sentences = nltk.sent_tokenize(post) [1]
		sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
		sentences = [nltk.pos_tag(sent) for sent in sentences]
		grammar = "NP: {<DT>?<JJ>*<NN>}"
		cp = nltk.RegexpParser(grammar)
		result = cp.parse(sentences[0])
		print result"""
