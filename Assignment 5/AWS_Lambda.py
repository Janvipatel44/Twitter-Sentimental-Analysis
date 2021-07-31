import json 
import boto3 

def lambda_handler(event, context): 
    client = boto3.client('sqs', region_name='us-east-1', aws_access_key_id="ASIAWXU5W2ERNLBLULMT",
    aws_secret_access_key="ZHuC0MeKyzsvhlaKH3r7p5xSM8eHyR92nRBT7Y06",
    aws_session_token="FwoGZXIvYXdzELP//////////wEaDBQy1+kM2nv3AliAMSK/Abm+wK3LjYmEEQ5DJjP5DXpG27FBgo2/libXJx682zJIc8cD+GXy1q5kx5ICpvKSdWdwFCkx7Exowq/DHKH/M500lL+Vr+DDrFH8f2kcuDFhy181IQI1rwF8mTXWwBnVhszsjjVL+GajN+d5SaJo8Jaeon/8i9zdsHbhJRY0y225Jk6g4t4JW0coGDmwOW8S2T+53hvcAUSLjUauWrMjf4DI/tPmR+ny5FupsGPYupQg2k29FvtLvh6CT5tYTbWrKKjqkIgGMi3QpasN9aPXSPLbGsFXHFk2pKm5hxRoTR0EK0MxopADNla7hPgKRGDbCCCDZHc=")
    
    response = client.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/463113474338/assignment5B00863421')
    print("Message from AWS:", response['Messages'][0]['Body']) 
    message = response['Messages'][0] 
    messageData = message['Body'] 
    
    snsClient = boto3.client('sns') 
    snsClient.publish(TopicArn = 'arn:aws:sns:us-east-1:463113474338:assignment5PartB', Message = 'Your order is ready. Please collect your bouquet provided to the door.' + messageData, Subject = 'Your Order is Ready') 
    Order_handle = message['ReceiptHandle'] 
    res = client.delete_message( QueueUrl="https://sqs.us-east-1.amazonaws.com/463113474338/assignment5B00863421", ReceiptHandle=Order_handle)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
