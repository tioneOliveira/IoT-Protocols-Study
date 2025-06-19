import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "home/+/temperature"
PANEL_ID = "control_panel"

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload.decode())
        sensor_id = message["sensor_id"]
        temperature = message["temperature"]
        print(f"Recieved from {sensor_id}: {temperature}°C")
    except Exception as e:
        print(f"Something went wrong in the message processing {e}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Panel connected into the BROKER")
        client.subscribe(TOPIC)
        print(f"Panel subscribed into the topic: {TOPIC}")
    else:
        print(f"Something went wrong in connection, code: {rc}")
        
client = mqtt.Client(client_id=PANEL_ID)
client.on_message = on_message
client.on_connect = on_connect

client.connect(BROKER, PORT)
client.loop_forever()

