#!/usr/bin/env python
import pika
import time

# Establish a connection to rabbitmq server
credentials = pika.PlainCredentials('admin', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.193.230.56', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(5)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()