from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC624f172a6db0c9574c57ad67b424e02b" 
AUTH_TOKEN = "dbbedf933cb071523f8ad0ba9f436bd7" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

import random

numbers = {
	"Eric":   "+17038190161",
	"Daniel": "+17039551026",
	"Adam":   "+17039157591",
	"Maia":   "+17038504482",
	"Rhonda": "+17038196104", 
	"Gary":   "+17038197172",
	"Kerry":  "+17035851585"
}

result = {}

counter = 0

while counter < len(numbers):
	
	[gifter, receiver] = random.sample(numbers, 2)
	
	if not gifter in result and gifter != receiver:
		result[gifter] = receiver
		counter += 1


for gifter, receiver in result.items():

	client.messages.create(
	    to=numbers[gifter], 
	    from_="+15406803234", 
	    body="Hi {0}, This is Moses, thou shall buy a gift for {1} by Sunday, Dec 6th. SHH!! Keep it a secret!".format(gifter, receiver), 
	    media_url="http://goo.gl/V7LVmi", 
	)
