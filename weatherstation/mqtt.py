import paho.mqtt.client as mqtt
import requests as req
from requests.auth import HTTPBasicAuth
import json

# MQTT Settings
# CloudMQTT Broker
MQTT_Broker = "postman.cloudmqtt.com"
MQTT_Port = 15589
# Local Mosquitto MQTT Broker
# MQTT_Broker = "192.168.43.95"
# MQTT_Port = 1883
MQTT_Username = "nswnnfoc"
MQTT_Password = "HbdSr-1z9oYG"
Keep_Alive_Interval = 60
MQTT_Topic = "AQMS/#"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK...")
        rc2 = client.subscribe(MQTT_Topic)
        if rc2[0] == 0:
            print("Subscribed to topic: "+MQTT_Topic)
        else:
            print("Error on subscribe: "+str(rc2))
    else:
        print("Bad Connection Return code=", rc)


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Client Subscribed...")


def on_publish(client, userdata, result):
    print("Data published...")


def on_message(mosq, obj, msg):
    from .store_sensor_data_to_db import sensor_data_handler
    # message in JSON format
    message = msg.payload.decode("utf-8")
    print("Received data: " + message)
    # This is the Master Call for saving MQTT Data into DB
    sensor_data_handler(message)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.username_pw_set(MQTT_Username, MQTT_Password)
client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)
client.publish("AQMS/station1", "test message1 from Django server")
client.publish("AQMS/station2", "test message2 from Django server")
