import praw
import time
import base64
import calendar
import unicodedata
import NameRecognition as nR
import MovieNameRecognition as mR

"""
Defines the mode that the bot will run in 
0 - Debug
1 - Release
"""
mode = 0
"""
Defines how often the bot will scan reddits.
0 - Only once
1 - Run Periodically
x - Run Periodically x number of times.

"""
period = 0

def main():
	bot = MediaRecognitionBot()
	
	bot.runBot()

class MediaRecognitionBot:
	
	def __init__(self):
		self.subsToPoll = []
		self.postsToPoll = []
		if mode == 1:
			self.subsToPoll = ["askreddit","movies"]
		if mode == 0:
			self.subsToPoll = ["MediaRecognitionBot"]
			self.postsToPoll = ["http://www.reddit.com/r/Python/comments/1slti5/can_you_lend_me_a_hand_with_generating_some_test/"]
		
		self.r = None
		#Is the bot loged on to its account
		self.isLogedIn = False
		
		#Dictionary of which posts have been analized and the number of comments looked at.
		self.postAnalized = { }
		
		self.mediaRecog = nR.mediaNameRecognition()
		self.movieRecog = mR.movieNameRecognition()
		
		
	def gatherPosts(self):
		None
		
	def generateResponse(self):
		None
		
	"""
	Posts a reply to a particular comment.
	"""
	def postToComment(self,post,comment):
		comment.reply(post)
	
	"""
	Attempts to log the bot in and updates the class isLogged in variable
	"""
	def login(self):
		#probibly a bad idea to hardcode the password.
		self.r.login("MediaRecognitionBot",base64.b64decode("TVJCRGFuaWVsNjk="))
		self.isLogedIn = self.r.is_logged_in()
	
	def analyzeComments(self, comments):
		for comment in comments:
			#mediaRecog.runMediaRecognition("Lord of the Rings is a very good movie.")
			names = self.mediaRecog.runMediaRecognition(unicodedata.normalize('NFKD', comment.body).encode('ascii','ignore'))
			for name in names:
				print name
				self.movieRecog.runRecognition(name)
			"""try:
				names = self.mediaRecog.runMediaRecognition(unicodedata.normalize('NFKD', comment.body).encode('ascii','ignore'))
				for name in names:
					print name
					self.movieRecog.runRecognition(name)
					
			except UnicodeEncodeError:
				None
			except AttributeError:
				None
			"""	
			
	def runBot(self):
		self.r = praw.Reddit(user_agent='MediaRecocnitionBot 0.3 by u/insaneHoshi')
		print self.subsToPoll

		self.login()
		print self.isLogedIn
		
		timesRun = 0
		while True:
			for sub in self.subsToPoll:
				submissions = self.r.get_subreddit(sub).get_hot(limit = 10)
				
				for submission in submissions:
					
					comments = praw.helpers.flatten_tree(submission.comments)
					self.postAnalized[submission.short_link] = len(comments)
					
					
					# If the post is more than an hour old or its comments are more than 2000 (ie this has probibly looked at it allready)
					if submission.created_utc < (calendar.timegm(time.gmtime()) - 3600) or len(comments) <= 2000:
						
						self.analyzeComments(comments)
					
			timesRun +=1
			if period >= 1:
				time.sleep(3600)
				
			if period == 0 or (period >1 and timesRun >period):
				break
				
		if mode == 0:
			for post in self.postsToPoll:
				submission= self.r.get_submission(post)
				comments = praw.helpers.flatten_tree(submission.comments)
				
				self.analyzeComments(comments)
				
			
					
					
						
if __name__ == "__main__":
	main();
	

