# -*- coding: utf-8 -*-


import boto3
import time
import random

client = boto3.resource('sqs', region_name='us-east-1')

queue = client.get_queue_by_name(QueueName='assignment5B00863421')

OrderMessage = ['Please confirm order for a fabulous collection of white and cream flowers make this the perfect gift',
                '5 Mamma Mia order is placed',
                'Can you provide Orchid bouquet at 1991 brunswick street?',
                'I have received wrong order for Tulip bouquet',
                'Do you have white peaceful lily bouquet today?']

Size = ['LARGE', 'MEDIUM', 'SMALL', 'JUNIOR', 'MINI', 'TOSS', 'WAND']


def sendToSQS():
    while True:
        bouquetOrderMessage = (random.choice(OrderMessage))
        bouquetSize = random.choice(Size)
        sendData = bouquetOrderMessage + " " + bouquetSize
        response = queue.send_message(MessageBody= sendData)
        print(response)
        time.sleep(300)


sendToSQS()





