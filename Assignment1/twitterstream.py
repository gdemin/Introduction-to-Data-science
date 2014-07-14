import oauth2 as oauth
import urllib
import urllib2
import json

api_key = "uh17pit6qMXu8S2ASBRAvTcCI"
api_secret = "JzMNKwVj0iDkssDtfX3RbgTGHa0OAULVAjNpvQsCs2Ltx9eMit"
access_token_key = "25037696-wR32LYh9PVzfeJVXuYY03ksihMCpUF8JWO47GjPVP"
access_token_secret = "dx8BlAvhtRpOdCshRjENgpT0IDwBBdtcpQ0nz1CAGAm9S"

consumer = oauth.Consumer(key=api_key, secret=api_secret)
access_token = oauth.Token(key=access_token_key, secret=access_token_secret)
client = oauth.Client(consumer, access_token)

search_string ="https://api.twitter.com/1.1/search/tweets.json?q=crimea"
max_request = 100000
for i in range(max_request):
	response, data = client.request(search_string)
	tweets = json.loads(data)
	# print tweets
	# print response
	
	min_id = min([status["id"] for status in tweets["statuses"]])
	for status in tweets["statuses"]:
		print status["text"]
	search_string ="https://api.twitter.com/1.1/search/tweets.json?q=crimea&max_id=" + str(min_id-1)
