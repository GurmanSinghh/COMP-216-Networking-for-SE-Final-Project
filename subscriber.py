import json
import paho.mqtt.client as mqtt
import util

 

def on_connect(mqttc, userdata, flags, rc):
    print('connected...rc=' + str(rc))
    mqttc.subscribe(topic='network/#', qos=0)


def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))


def on_message(mqttc, userdata, msg):
    print("Received message --------")
    print('topic: ' + msg.topic + ', qos: ' + 
          str(msg.qos) + ', message: ' + str(msg.payload))
    decode_msg(msg.payload)    


def on_subscribe(mqttc, userdata, mid, granted_qos):
    print('subscribed (qos=' + str(granted_qos) + ')')


def on_unsubscribe(mqttc, userdata, mid, granted_qos):
    print('unsubscribed (qos=' + str(granted_qos) + ')')


def decode_msg(msg):
    msg = msg.decode('utf-8')
    payload = json.loads(msg)
    print("\n-------- Decoded msg -----------\n")
    util.print_data(payload)


mqttc = mqtt.Client()

mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe
mqttc.connect(host='broker.emqx.io', port=1883)

mqttc.loop_forever()