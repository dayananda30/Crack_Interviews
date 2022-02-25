#!/usr/bin/env python
import pika
import sys

# Establish a connection to rabbitmq server
credentials = pika.PlainCredentials('admin', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.193.230.56', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

for message in range(101):
    message = "message-{}".format(message)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(" [x] Sent %r" % message)
connection.close()