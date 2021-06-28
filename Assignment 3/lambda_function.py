import boto3
import pymysql
import json


def read_file(bucketname, itemname):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucketname, itemname)
    for obj in obj.all():
        body = obj.get()['Body'].read()
        content = body.decode('utf-8')
        json_content = json.loads(content)
        sqlOperations(json_content, itemname)
    return words


for i in range(1, 401):
    inp_file_name = "D:/Study D/Dalhousie/Sem 3/Serverless/Assignments/Assignment 3/tech/" + str(i) + ".txt"
    inp_file_key = str(i) + ".txt"
    s3_bucket_name = "tagb00863421"
    read_file(s3_bucket_name, inp_file_key)


def sqlOperations(json_content,itemname):
    # Connect to the database
    connection = pymysql.connect(host='database-assignment3.cik0ja21ushh.us-east-1.rds.amazonaws.com',
                                 user='janvi',
                                 password='Admin#123',
                                 db='wordCount_asssignment3')

    cursor = connection.cursor()
    sql = "INSERT INTO `FrequencyCalculator` (`NamedEntity`, `FrequencyCount`) VALUES (%s, %s)"
    itemname = itemname.replace(".txt", "")

    for key in json_content[itemname][0]:
        value = json_content[itemname][0][key]
        cursor.execute(sql, (key, value))

    connection.commit()
    cursor.close()
