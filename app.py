from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import urllib
import csv
from bot import get_data
import os
app = Flask(__name__)
@app.route("/")
def hello():
    return("Hey")
@app.route("/sms", methods=['POST','GET'])
def sms_reply():
    msg= request.form.get('Body')
    answer = get_data(msg)
    print(type(answer))
    response = MessagingResponse()
    resp = response.message(answer)
    return str(response)
    

if __name__ == "__main__":
    
    app.run(port = 5001)


