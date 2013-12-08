import praw
import time
import base64

"""
Defines the mode that the bot will run in 
0 - Debug
1 - Release
"""
mode = 0

def main():
	bot = MediaRecognitionBot()
	
	bot.runBot()

class MediaRecognitionBot:
	
	def __init__(self):
		self.subsToPoll = []
		if mode == 1:
			self.subsToPoll = ["programming"]
		if mode == 0:
			self.subsToPoll = ["MediaRecognitionBot"]
			
		self.r = None
		#Is the bot loged on to its account
		self.isLogedIn = False
		
	def gatherPosts(self):
		None
		
	def generateResponse(self):
		None
		
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
		self.r = praw.Reddit(user_agent='MediaRecocnitionBot 0.1 by u/insaneHoshi')
		print self.subsToPoll
		
		self.login()
		print self.isLogedIn
		for sub in self.subsToPoll:
			subreddit =self.r.get_subreddit(sub)
			submissions = self.r.get_subreddit(sub).get_hot(limit = 1)
			
			for submission in submissions:
				
				comments = praw.helpers.flatten_tree(submission.comments)
				for comment in comments:
					try:
						print comment.body
						
					except:
						None
					
if __name__ == "__main__":
	main();
	

