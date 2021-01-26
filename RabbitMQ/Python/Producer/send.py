import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.15.13.154'))
channel = connection.channel()

channel.queue_declare(queue='QUEUE_TEST')

channel.basic_publish(exchange='', routing_key='QUEUE_TEST', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()