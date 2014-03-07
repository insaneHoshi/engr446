import imdb
import Levenshtein
import unicodedata
from operator import itemgetter

"""
The min Levenshtein distance to consitute a match

"""
minLevenshtein = 0.79



class movieNameRecognition:
	def __init__(self):
		self.ia = imdb.IMDb() # by default access the web.

	
	def isMatch(self,possibleTitle, title):
		isMatch = False
		closeness = 0
		
		ratio = Levenshtein.ratio(possibleTitle, unicodedata.normalize('NFKD', title).encode('ascii','ignore'))
		
		if ratio >= minLevenshtein:
			isMatch = True
			closeness = ratio
		
		return isMatch,closeness 
		
	def runRecognition(self,possibleTitle):
		results = []
		s_result = ""
		
		try:
			s_result = self.ia.search_movie(possibleTitle)
			print s_result
		except imdb.IMDbError:
			print "Probably you're not connected to Internet."
			
			return []
		
		
		for item in s_result:
			title = item['long imdb canonical title']
			title = title.rsplit("(")[0]
			if ", The" in title:
				title = "The " +title.strip(", The")
			
			
			isMatch, closeness = self.isMatch(possibleTitle, title)
			if(isMatch):
				results.append([closeness,item])
		
		results = sorted(results,key=itemgetter(1))
		print results
		
		
