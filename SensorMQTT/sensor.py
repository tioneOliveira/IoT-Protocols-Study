import paho.mqtt.client as mqtt
import random
import time
import json

BROKER = "localhost"
PORT = 1883
SENSOR_ID = "sensor_1"
TOPIC = "home/1/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"{SENSOR_ID} connected into the BROKER")
    else:
        print(f"Something went wrong in connection, code: {rc}")

client = mqtt.Client(client_id=SENSOR_ID)
client.connect(BROKER, PORT)
client.on_connect = on_connect

client.loop_start()

try:
    while True:
        randNumber = round(random.uniform(20.0, 21.0), 2)
        message = {"sensor_id": SENSOR_ID,
                   "temperature": randNumber,
                   "timestamp": time.time()}
        client.publish(TOPIC, json.dumps(message))
        print(f"{SENSOR_ID} published: {message} into topic: {TOPIC}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Connection_Terminated")
    client.loop_stop()
    client.disconnect