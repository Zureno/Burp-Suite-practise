import slack
 
SLACK_TOKEN="xoxb-4669670075472-4650065173316-2frXG653NwD7e0HT2EPnrgZE" 
client = slack.WebClient(token=SLACK_TOKEN)
client.chat_postMessage(channel='#testing',text='How are you')