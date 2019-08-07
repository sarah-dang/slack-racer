import os
import slack

token = 'xoxb-707886202387-721598349094-Z2VDHIYjrumQbqmUUNlvMu0j'
client = slack.WebClient(token=token)

'''
response = client.chat_postMessage(
    username="Slack Racer Referee",
    icon_emoji=":checkered_flag:",
    channel="general",
    text="Sahand is the BEST.",
)
'''

import asyncio

loop = asyncio.get_event_loop()

client = slack.WebClient(
    token=token,
    run_async=True
    )

response = loop.run_until_complete(client.chat_postMessage(
        channel='#random',
        text="Hello world!"
        )
        )
        
assert response["ok"]
assert response["message"]["text"] == "Hello world!"
