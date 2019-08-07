import os
import slack

token = 'xoxb-707886202387-721598349094-Z2VDHIYjrumQbqmUUNlvMu0j'
client = slack.WebClient(token=token)

response = client.chat_postMessage(
    username="Slack Racer Referee",
    icon_emoji=":bearded_person:",
    channel="general",
    text="Sahand is the BEST.",
)
