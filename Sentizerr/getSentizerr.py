#install microsoft essential tools
# install textblob
# !pip install azure-ai-textanalytics --pre

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

#read azure credentials
azurekeyfile = open('azurekeys.key', 'r').read().splitlines()
key = azurekeyfile[0]
endpoint = azurekeyfile[1]

#read twitter dev credentials
twitterkeyfile = open('twitterkeys.key', 'r').read().splitlines()
twitterapikey = twitterkeyfile[0]
twitterapikeysecret = twitterkeyfile[1]
twitterbearertoken = twitterkeyfile[2]
twitteraccesstoken = twitterkeyfile[3]
twitteraccesstokensecret = twitterkeyfile[4]

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()


def sentiment_analysis_example(client):
	documents = ["prices are"]
	response = client.analyze_sentiment(documents=documents)[0]
	print("Document Sentiment: {}".format(response.sentiment))
	print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
		response.confidence_scores.positive,
		response.confidence_scores.neutral,
		response.confidence_scores.negative,
	))
	for idx, sentence in enumerate(response.sentences):
		print("Sentence: {}".format(sentence.text))
		print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
		print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
			sentence.confidence_scores.positive,
			sentence.confidence_scores.neutral,
			sentence.confidence_scores.negative,
		))


sentiment_analysis_example(client)