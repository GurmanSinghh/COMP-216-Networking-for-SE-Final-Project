import json
import util
import time, sys
import paho.mqtt.client as mqtt


def on_connect(mqttc, userdata, flags, rc):
    print('connected...rc=' + str(rc))


def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))


def on_message(mqttc, userdata, msg):
    print('message received...')
    print('topic: ' + msg.topic + ', qos: ' + 
          str(msg.qos) + ', message: ' + str(msg.payload))


def on_publish(mqttc, userdata, mid):
    print("Message published ID :{}".format(mid))


mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.connect(host='broker.emqx.io', port=1883)

max_msg = 2
count = 0
while True:
    try:
        msg_dict = util.create_data()    
        data = json.dumps(msg_dict)
        mqttc.publish(topic='network', payload=data, qos=0)
        print("Published msg: {}".format(msg_dict))
        count += 1
        if count >= max_msg:
            break  
        time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        mqtt.disconnect()
        sys.exit()

mqttc.disconnect()