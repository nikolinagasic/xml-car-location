import pika
import json
from script import get_points_along_path

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='location')

def callback(ch, method, properties, message):
    # print(" [x] Received %r" % androidToken)
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='latlng')
    if (message.decode('utf-8').strip('\"').split()[0] == "asdfghtrlo"):
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","FTN, Novi Sad",  "centar, Indjija", departure_time=None, period=2)
    elif (message.decode('utf-8').strip('\"').split()[0] == "asefghjklo"):
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","Mise Dimitrijevica, Novi Sad",  "bazen, Srpska Crnja", departure_time=None, period=2)
    elif (message.decode('utf-8').strip('\"').split()[0] == "asdfyyjklo"):
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","Janka Veselinovica, Novi Sad",  "skola, Ravno selo", departure_time=None, period=2)
    elif (message.decode('utf-8').strip('\"').split()[0] == "asdfghjklo"):
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","402 Rebecca Rd, Bethany Beach",  "Seacrets, OceanCity", departure_time=None, period=2)
    elif (message.decode('utf-8').strip('\"').split()[0] == "asdfghtklo"):
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","Griffith observatory, Los Angeles",  "Venice beach, Los Angeles", departure_time=None, period=2)
    else:
        points = get_points_along_path("AIzaSyBcBUQxfS6JldNG0Ltoju5YxE_0-CKJsu4","FTN, Novi Sad",  "Puskinova 8, Novi Sad", departure_time=None, period=2)
    key = int(message.decode('utf-8').strip('\"').split()[1])
    try:
        coordinates = {'lat': points[key][0], 'lng': points[key][1], 'androidToken' : message.decode('utf-8').strip('\"').split()[0], 'seconds' : message.decode('utf-8').strip('\"').split()[1]}
    except:
        coordinates = {'lat': points[len(points)*2-2][0], 'lng': points[len(points)*2-2][1], 'androidToken' : message.decode('utf-8').strip('\"').split()[0], 'seconds' :'-1'}
    channel.basic_publish(exchange='latlng-exchange', routing_key='latlng-key', body=json.dumps(coordinates))
    print(key)
    connection.close()

channel.basic_consume(
    queue='location', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

