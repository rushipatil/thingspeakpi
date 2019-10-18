MQTT:
Install Mosquitto on ras pi:-

sudo apt-get update
sudo apt-get install mosquito
sudo apt-get install mosquitto-clients
sudo pip install paho-mqtt

MQTT CLIENT:

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "hello":
        print("Received message #1, do something")

    if msg.payload == "World!":
        print("Received message #2, do something else")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()


MQTT SERVER :

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "hello", hostname="test.mosquitto.org")

publish.single("CoreElectronics/test", "World!", hostname="test.mosquitto.org")
print("Done")