import json
import re
import boto3
import string


#Based on https://medium.com/analytics-vidhya/working-with-twitter-data-b0aa5419532


#removing URL and Email from Tweet text
def removeUrl(string):
    string = str(string)
    string = re.sub(r'RT ','', string, flags=re.MULTILINE)
    string = re.sub(r'https?:\/\/ (www\.)?[-a-zA-Z0–9 @:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', "", string,
                    flags=re.MULTILINE)
    string = re.sub(r'[-a-zA-Z0–9 @:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', "", string, flags=re.MULTILINE)
    return string


#removing noise such as mentions, hashtags and tags
def removeNoiseWords(string):
    string = str(string)
    string = ' '.join(re.sub("(@[A-Za-z0–9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", string).split())
    return string


#removing numbers
def removeNumbers(string):
    string = str(string)
    string = re.sub(r"\d", "", string)
    return string


def lambda_handler(event, context):
    s3 = boto3.client('s3')

    sourceBucketName = "twitterdatab00863421"
    fileName = "file_mongo_tweets.txt"
    targetBucketName = "twitteranalysisb00863421"
    targetFileName = "twitteranalysisb00863421.csv"

    bucketObject = s3.get_object(Bucket=sourceBucketName, Key=fileName)
    fileContent = bucketObject['Body'].read().decode('utf-8')
    fileLines = fileContent.split('\n')
    comprehendObject = boto3.client('comprehend', region_name='us-east-1')

    cleanTweets = []
    output = 'Tweet, Sentiment, Positive Sentiment Score, Negative Sentiment Score, Neutral Sentiment Score, Mixed Sentiment Score'

    for line in fileLines:
        line = line.translate(str.maketrans('', '', string.punctuation))
        cleanLine = removeUrl(line)
        cleanLine = removeNumbers(cleanLine)
        cleanLine = removeNoiseWords(cleanLine)
        cleanTweets.append(cleanLine)

    for (index, item) in enumerate(cleanTweets):
        # So as not to exhaust credits of AWS.
        if index <= 9 and item != '':
            result = comprehendObject.detect_sentiment(Text=item, LanguageCode='en')
            finalOutput = finalOutput + '\n' + item + ',' + result['Sentiment'] + ',' + str(
                result['SentimentScore']['Positive']) + ',' + str(result['SentimentScore']['Negative']) + ',' + str(
                result['SentimentScore']['Neutral']) + ',' + str(result['SentimentScore']['Mixed'])

    print(finalOutput)
    s3.put_object(Bucket=targetBucketName, Key=str(targetFileName), Body=finalOutput)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }