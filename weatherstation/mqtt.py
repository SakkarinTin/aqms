import paho.mqtt.client as mqtt
import requests as req
from requests.auth import HTTPBasicAuth
import json

# api_key = '4d041f4c-8326-4fa4-b41e-3e458c107a01'
# api_url = 'https://api.cloudmqtt.com/api/user'
# data = {"username":"test", "password":"super_secret_password"}
# headers = {'Content-Type': 'application/json'}
# response = req.post(api_url, data, headers=headers, auth=('', api_key))
#
# print(data)
# print(response.text)
# print("Hello World")

# MQTT Settings
MQTT_Broker = "postman.cloudmqtt.com"
MQTT_Port = 15589
Keep_Alive_Interval = 45
MQTT_Topic = "hexiwear/sensor"
MQTT_Username = "nswnnfoc"
MQTT_Password = "HbdSr-1z9oYG"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK...")
        client.subscribe(MQTT_Topic)
    else:
        print("Bad Connection Return code=", rc)


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Client Subscribed...")


def on_publish(client,userdata,result):
    print("Data published...")


def on_message(mosq, obj, msg):
    from .store_sensor_data_to_db import sensor_data_handler
    # message in JSON format
    message = msg.payload.decode("utf-8")
    print("Received data from Hexiwear...")
    print(message)
    # This is the Master Call for saving MQTT Data into DB
    sensor_data_handler(msg.topic, message)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.username_pw_set(MQTT_Username, MQTT_Password)
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.publish(MQTT_Topic, "MQTT Message from Django Server")
