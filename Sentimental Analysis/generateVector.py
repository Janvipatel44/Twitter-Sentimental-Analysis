# ------------------------------------------------------------------------------------------------------------------------
import json

import boto3
import stringdist


def s3_client():
    """
        Function: get s3 client
         Purpose: get s3 client
        :returns: s3
    """
    session = boto3.session.Session()
    client = session.client('s3')
    """ :type : pyboto3.s3 """
    return client


def writeContent(distance):
    # push the content in the csv file
    s3 = boto3.resource('s3')
    bucketName = "traindatab00863421"
    fileName = "trainVector.csv"
    s3.Object(bucketName, fileName).put(Body=distance)
    print('Successfully generation of trainVector.csv on bucket named - traindatab00863421')


def levenshtein_distance_gen(filteredWords):
    listContent = ""
    # find out levenshtein distance between current and next word
    for i in range(len(filteredWords) - 1):
        currentWord, nextWord = filteredWords[i], filteredWords[i + 1]
        count = stringdist.levenshtein(currentWord, nextWord)
        body = currentWord + "," + nextWord + "," + str(count)
        listContent = listContent + '\n' + body
    headers = "Current_Word" + "," + "Next_Word" + "," + "Levenshtein_distance" + '\n'
    distance = headers + listContent
    print(distance[0:120])
    writeContent(distance)

def removeStopWords(content):
    # https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
    # https://www.tutorialspoint.com/python_text_processing/python_remove_stopwords.htm
    stopWords = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once',
                 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some',
                 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other',
                 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves',
                 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me',
                 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while',
                 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
                 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves',
                 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under',
                 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i',
                 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it',
                 'how', 'further', 'was', 'here', 'than', 'your', u'yours', u'yourself', u'yourselves', u'he',
                 u'him', u'his', u'himself', u'she',
                 u"she's", u'her', u'hers', u'herself', u'it', u"it's", u'its', u'itself', u'they', u'them',
                 u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this',
                 u'that', u"that'll", u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be',
                 u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing',
                 u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until',
                 u'while', u'of', u'at']
    content = content.lower()
    words = content.split()
    filteredWords = [word for word in words if not word in stopWords]
    levenshtein_distance_gen(filteredWords)


def lambda_handler(event, context):
    s3_bucket_name = "sourcedatab00863421"
    s3 = boto3.resource('s3')
    obj = s3.Bucket(s3_bucket_name)
    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    filesContent = ""
    for obj in obj.objects.all():
        body = obj.get()['Body'].read()
        content = body.decode('utf-8')
        filesContent = filesContent + content
    removeStopWords(filesContent)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

#https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python



