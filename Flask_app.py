import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
from flask_ngrok import run_with_ngrok
 

SLACK_TOKEN="xoxb-4669670075472-4650065173316-2frXG653NwD7e0HT2EPnrgZE"
SIGNING_SECRET="78e8daf8de4a102dc76cb9c2e67e0ae4"
 
app = Flask(__name__)
run_with_ngrok(app)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
client = slack.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='#testing',text='Hello World!')
 
 
if __name__ == "__main__":
    app.run()