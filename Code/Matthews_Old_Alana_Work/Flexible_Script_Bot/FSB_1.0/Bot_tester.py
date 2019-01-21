import json#needed for json manipulation (state is json data)

import requests#used for testing


#this is for TEST PURPOSES ONLY. This program will (hopefully) allow for unit testing of the bots, simulating the Alana system as a whole.


CarryOn = True

Conversation = ""#the conversational string


while CarryOn == True:

    try:#ensures graceful failure in the event of an exception

        r = requests.post('http://0.0.0.0:5111/', json={'state' : {'input' : {'text' : "hello"}}})

        r.json()#if the response is not proper json, it should crash here

        data = json.loads(r.text)[0]

        print("the bot is called " + data["bot_name"])

    except:

        CarryOn = False
