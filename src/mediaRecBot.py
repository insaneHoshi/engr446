import praw
import time
import base64
import calendar
import unicodedata
import NameRecognition as nR

"""
Defines the mode that the bot will run in 
0 - Debug
1 - Release
"""
mode = 1
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
		if mode == 1:
			self.subsToPoll = ["askreddit"]
		if mode == 0:
			self.subsToPoll = ["MediaRecognitionBot"]
			
		self.r = None
		#Is the bot loged on to its account
		self.isLogedIn = False
		
		#Dictionary of which posts have been analized and the number of comments looked at.
		self.postAnalized = { }
		
		
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
		
	def runBot(self):
		self.r = praw.Reddit(user_agent='MediaRecocnitionBot 0.2 by u/insaneHoshi')
		print self.subsToPoll
		mediaRecog = nR.mediaNameRecognition()
		self.login()
		print self.isLogedIn
		
		timesRun = 0
		while True:
			for sub in self.subsToPoll:
				subreddit =self.r.get_subreddit(sub)
				submissions = self.r.get_subreddit(sub).get_hot(limit = 10)
				
				for submission in submissions:
					
					comments = praw.helpers.flatten_tree(submission.comments)
					self.postAnalized[submission.short_link] = len(comments)
					
					
					# If the post is more than an hour old or its comments are more than 2000 (ie this has probibly looked at it allready)
					if submission.created_utc < (calendar.timegm(time.gmtime()) - 3600) or len(comments) <= 2000:
						
						for comment in comments:
							
							try:
								mediaRecog.runMediaRecognition(unicodedata.normalize('NFKD', comment.body).encode('ascii','ignore'))
								
							except UnicodeEncodeError:
								None
							except AttributeError:
								None
							
			timesRun +=1
			if period >= 1:
				time.sleep(3600)
				
			if period == 0 or (period >1 and timesRun >period):
				break
				
if __name__ == "__main__":
	main();
	

