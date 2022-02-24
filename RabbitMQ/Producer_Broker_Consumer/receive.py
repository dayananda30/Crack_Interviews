import os
import sys
import pika


def main():
    """
    First we need to connect to RabbitMQ server.
    Establish a connection to rabbitmq server
    """
    credentials = pika.PlainCredentials('admin', 'password')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='10.193.230.56', port=5672, credentials=credentials))
    channel = connection.channel()

    """
    The next step, just like before, is to make sure that the queue 
    exists. Creating a queue using queue_declare is idempotent ‒ 
    we can run the command as many times as we like, and only one will be created
    """

    channel.queue_declare(queue='nanda')

    """Receiving messages from the queue is more complex. It works by subscribing a callback function to a queue. 
    Whenever we receive a message, this callback function is called by the Pika library. In our case this function will 
    print on the screen the contents of the message. """

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='nanda',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(0)
