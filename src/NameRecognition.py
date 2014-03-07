import nltk
import numpy
from nltk.corpus import treebank
from nltk.tree import *
from nltk.draw import tree
import re

"""
Defines the number (one indexed) of non nouns that can seperate nouns, so that the whole
pharse is considered a Proper Noun, ie Lord of the Rings would be considered a 
PN if numWrdDeliter >=1
"""
numWrdDelimiter = 2

class mediaNameRecognition:
	def __init(self):
		None
	
	"""
	Takes a human readable sentance and creates a parse tree defining
	the proper nouns contained within this sentence.  
	
	It then returns a list of proper nouns.
	
	"""
	def namedEntityRecognition(self,sentence):
		tokens = nltk.word_tokenize(sentence)
		
		pos_tags = nltk.pos_tag(tokens)
		#print nltk.ne_chunk(pos_tags, binary=True)
		grammar = "NP: {<DT|PP\$>?<JJ>*<NNP>+}"
		"""
		NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and proper nouns
		      {<NNP>+}                # chunk sequences of proper nouns
		"""
		
		cp = nltk.RegexpParser(grammar)
		tree = cp.parse(pos_tags)
		
		possibleTitles = []
		possibleTitle = ""
		possibleDelimTitle = ""
		delimCounter = 0
		delimBool = False
		tree.draw()
		for subtree in tree:
			if str(type (subtree)) == "<type 'tuple'>":
				if delimBool ==True:
					delimCounter+=1
					possibleDelimTitle +=subtree[0]+" "
				
				if delimCounter > numWrdDelimiter:
					delimBool = False
					delimCounter = 0
					possibleDelimTitle = ""
				possibleTitle = ""
			else:
			
				if subtree.node == "NP":

					firstLeaf = subtree.leaves()[0]
					firstString = firstLeaf[0]
					#print subtree
					if firstString.endswith("."):
						#check first leaf to see if a leaf of a
						#subtree begins with a string with a period
						#and the end.  This happens sometimes when a
						#PN begins a sentence, the previouse tuple gets
						#included as a PN
						subtree.pop(0)
					
					if len(subtree)>1:
						
						for leaf in subtree.leaves():
							possibleTitle +=leaf[0]+" "
						
						possibleTitles.append(possibleTitle.strip())
						
					
					if len(subtree)>=1:
						#try to concat a movie title if its seperated by non nouns
						
						
						for leaf in subtree.leaves():
							possibleDelimTitle +=leaf[0]+" "
						
						if delimCounter > 0:
							#the tail end of the split proper noun
							possibleTitles.append(possibleDelimTitle.strip())
							
						
						#reset the counter
						delimBool = True
						delimCounter = 0
				
			
		for title in possibleTitles:
			#if we have a title with all caps we can discard this with high confidence
			titleClean = re.sub(r'\W+', ' ', title)
			if titleClean.isupper():
				possibleTitles = []
			
			if "." in title:
				
				#sometimes the NLTK will say "Jump Street. I"
				#instead of "Jump Street", this alters this case
				possibleTitles[possibleTitles.index(title)]= title.split(".")[0]

			if " 's" in title:
				possibleTitles[possibleTitles.index(title)]= title.replace(" 's","'s")
		return possibleTitles
		
			
			
			
		
	def runMediaRecognition(self, sentence):
		
		titles = self.namedEntityRecognition(sentence)
		return titles
