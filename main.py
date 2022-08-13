import praw
import time
import random
import requests
import json
from time import sleep
from random import randint

while True:
	rand = randint(0,4)
	rand2 = randint(0,4)

	list_subr = [""]
	subreddit = list_subr[rand]
	count = 1
	timeframe = 'all' #hour, day, week, month, year, all
	listing = 'random' # controversial, best, hot, new, random, rising, top
	def get_reddit(subreddit,count):
		try:
		    base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
		    request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
		except:
		    print('An Error Occured')
		return request.json()
		 
	top_post = get_reddit(subreddit,count)
		 
	if listing != 'random':
	    title = top_post['data']['children'][0]['data']['title']
	    url = top_post['data']['children'][0]['data']['url']
	else:
	    title = top_post[0]['data']['children'][0]['data']['title']
	    url = top_post[0]['data']['children'][0]['data']['url']
		 
		 
	try:
		filename = '1.jpg'
		res = requests.get(url)
		print(res.status_code)
		with open(filename, 'wb') as out:
		    out.write(res.content)
		    print("Downloaded")
	except:
		print("Failed to download!")

	reddit = praw.Reddit(client_id="",
	                     client_secret="",
	                     user_agent="",
	                     username="",
	    				 password="")



	subr = list_subr[rand2] # Choose your subreddit

	image = "1.jpg"
	reddit.subreddit(subr).submit_image(title, image)
	print("Uploaded")
	print("Sleeping 15 mins")
	sleep(900)
