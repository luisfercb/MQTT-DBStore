import sqliteMgr
import datetime
import paho.mqtt.client as mqtt

# MQTT Settings
MQTT_Broker = "192.168.1.50"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "sala/temperatura"
dataBase = "/home/luisfer/Documents/IOT/DataBase/iot.db"
cursor = ""


# Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
    mqttc.subscribe(MQTT_Topic)


# Save Data into DB Table
def on_message(mosq, obj, msg):
    timestamp = str(datetime.datetime.now())
    hora = timestamp.split('.', 1)
    print("MQTT Data Received...")
    print("MQTT Topic: " + msg.topic)
    print("Data: " + str(msg.payload.decode("utf-8")))
    mensaje = str(msg.payload.decode("utf-8"))
    Nodo = mensaje.split(":", 1)
    print(Nodo[0])
    print(hora[0])
    print(Nodo[1])
    sqliteMgr.insert_db(dataBase, "temp", str(Nodo[0]), str(hora[0]), int(Nodo[1]))


def on_subscribe(mosq, obj, mid, granted_qos):
    pass


mqttc = mqtt.Client("P1")

# Assign event callbacks
mqttc.on_message = on_message
# mqttc.on_connect = on_connect
# mqttc.on_subscribe = on_subscribe

# Connect
# mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.connect(MQTT_Broker)
mqttc.subscribe(MQTT_Topic)

# Continue the network loop
mqttc.loop_forever()
