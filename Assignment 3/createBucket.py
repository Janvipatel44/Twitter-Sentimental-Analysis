import boto3
import json


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


# ------------------------------------------------------------------------------------------------------------------------
def s3_create_bucket(bucket_name):
    """
        function: s3_create_bucket - create s3 bucket
           :args: s3 bucket name
        :returns: bucket
    """
    # fetch the region
    session = boto3.session.Session()

    # get the client
    client = s3_client()

    s3_bucket_create_response = client.create_bucket(Bucket=bucket_name)

    print(f" *** Response when creating bucket - {s3_bucket_create_response} ")
    return s3_bucket_create_response


def word_count(words, itemname):
    wdict = {}
    for word in words:
        if word[0].isupper():
            try:
                wdict[word] += 1
            except KeyError:
                wdict[word] = 1
    jsonFormat = "{'" + itemname +"ne" + "':[" + str(wdict) + "]}"
    jsonString = json.dumps(jsonFormat)
    return jsonString


def read_file(bucketname, itemname):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname, itemname)
    for obj in obj.all():
        body = obj.get()['Body'].read()
        content = body.decode('utf-8')
        words = content.split()
        namedEntity_bucket = "tagb00863421"
        s3_create_bucket(namedEntity_bucket)
        namedEntityItem = itemname.replace(".txt", "")
        jsonContent = word_count(words, namedEntityItem)
        print(jsonContent)
        s3.Object(namedEntity_bucket, namedEntityItem+"ne.txt").put(Body=jsonContent)


for i in range(1, 401):
    inp_file_name = "D:/Study D/Dalhousie/Sem 3/Serverless/Assignments/Assignment 3/tech/" + str(i) + ".txt"
    inp_file_key = str(i) + ".txt"
    s3_bucket_name = "sampledatab00863421"
    read_file(s3_bucket_name, inp_file_key)
