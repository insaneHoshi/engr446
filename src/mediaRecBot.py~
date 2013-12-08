import praw
import time

def main():
	bot = MediaRecognitionBot()
	
	bot.runBot()

class MediaRecognitionBot:
	def __init__(self):
		self.subsToPoll = ["programming"]
		
	def gatherPosts(self):
		None
		
	def generateResponse(self):
		None
		
	def runBot(self):
		r = praw.Reddit(user_agent='MediaRecocnitionBot 0.1 by u/insaneHoshi')
		print self.subsToPoll
		for sub in self.subsToPoll:
			
			submissions = r.get_subreddit(sub).get_top(limit = 1)
			try:
				while True:
					submission = next(submissions)
					comments = praw.helpers.flatten_tree(submission.comments)
					for comment in comments:
						print comment.body
			except StopIteration: 
				None

if __name__ == "__main__":
	main();
	

