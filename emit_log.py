#!/usr/bin/env python
import requests
import pika

valor = requests.get('https://brasilapi.com.br/api/cep/v1/04177370')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = str(valor.json())
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()