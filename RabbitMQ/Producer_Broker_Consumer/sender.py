import pika

# Establish a connection to rabbitmq server
credentials = pika.PlainCredentials('admin', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.193.230.56', port=5672, credentials=credentials))
channel = connection.channel()

# Create a queue before sending the message to broker
channel.queue_declare(queue="daya")
channel.queue_declare(queue="nanda")

"""
In RabbitMQ, a message can never be sent directly to the queue.
It always needs to go through an exchange

queue_name needs to be specified in the routing_key parameter.
"""


channel.basic_publish(exchange='',
                      routing_key='daya',
                      body='Hello Daya')
print(" [x] sent 'Hello Daya'")

# Close all conenctions

for item in range(50):
    item = "Item - {}".format(item)
    channel.basic_publish(exchange='',
                          routing_key='nanda',
                          body=item)
    print(" [x] sent '{}'".format(item))

connection.close()
