import time, requests, hmac, hashlib, json
import paho.mqtt.client as mqtt
import os

client_id = os.getenv("CLIENT_ID") or os.environ['CLIENT_ID']
client_secret = os.getenv("CLIENT_SECRET") or os.environ['CLIENT_SECRET']
device_id = os.getenv("DEVICE_ID") or os.environ['DEVICE_ID']
mqtt_topic = os.getenv("MQTT_TOPIC", "tuya/colonnina")
api_url = "https://openapi.tuyaeu.com"

def get_timestamp():
    return str(int(time.time() * 1000))

def sign_request(message, secret):
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest().upper()

def get_token():
    t = get_timestamp()
    message = client_id + t
    sign = sign_request(message, client_secret)

    headers = {
        "client_id": client_id,
        "sign": sign,
        "t": t,
        "sign_method": "HMAC-SHA256"
    }
    resp = requests.get(f"{api_url}/v1.0/token?grant_type=1", headers=headers)
    return resp.json()["result"]["access_token"]

def get_status(token):
    t = get_timestamp()
    message = client_id + token + t
    sign = sign_request(message, client_secret)

    headers = {
        "client_id": client_id,
        "access_token": token,
        "sign": sign,
        "t": t,
        "sign_method": "HMAC-SHA256"
    }
    resp = requests.get(f"{api_url}/v1.0/devices/{device_id}/status", headers=headers)
    return resp.json()["result"]

def publish_mqtt(data):
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.loop_start()
    client.publish(mqtt_topic, json.dumps(data), qos=1)
    client.loop_stop()
    client.disconnect()

# Loop infinito ogni 60 secondi
while True:
    try:
        token = get_token()
        status = get_status(token)

        parsed = {d["code"]: d["value"] for d in status}
        print("Stato colonnina:", parsed)
        publish_mqtt(parsed)

    except Exception as e:
        print("Errore:", e)

    time.sleep(60)
