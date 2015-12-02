from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

import random

numbers = {
	"Eric":   "+17038190161",
	"Daniel": "+17039551026",
	"Adam":   "+17039157591",
	"Maia":   "+17038504482",
	"Kerry":  "+17035851585",
}

usedReceivers = {}

result = {}

counter = 0

while counter < len(numbers):
	
	[gifter, receiver] = random.sample(numbers, 2)

	if not (gifter in result) and (gifter != receiver) and not (receiver in usedReceivers):
		result[gifter] = receiver
		usedReceivers[receiver] = 1
		counter += 1


for gifter, receiver in result.items():
	print [gifter, receiver]
	# Uncomment to send text messages
	# client.messages.create(
	#     to=numbers[gifter], 
	#     from_="+15406803234", 
	#     body="Hi {0}, This is Moses, thou shall buy a gift for {1} by Sunday, Dec 6th. SHH!! Keep it a secret!".format(gifter, receiver), 
	#     media_url="http://goo.gl/V7LVmi", 
	# )
