import os
import slack
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
    token = 'xoxb-707886202387-721598349094-Z2VDHIYjrumQbqmUUNlvMu0j'
    client = slack.WebClient(token=token)
    print(request)
    '''
    response = client.chat_postMessage(
        username="Slack Racer Referee",
        icon_emoji=":checkered_flag:",
        channel="general",
        text="Sahand is the BEST.",
    )
    '''
    return "Hello World!"

if __name__ == '__main__':
    app.run()