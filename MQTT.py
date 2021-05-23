import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.user_name_pw_set(username, password)

def pub_loop():
    i = 0
    qos = 0
    delay = 500
    client.connect("127.0.0.1", 1883, 60)
    #msg = subscribe.simple("test")
    #print(f"{msg.topic} {msg.payload}")
    while (i<=10):
        client.publish("test",f"{i}/{qos}/{delay}")
        time.sleep(delay/1000)
        i+=1
    client.disconnect()

def controller():
    client.subscribe(("request/qos","request/delay"))
    
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()