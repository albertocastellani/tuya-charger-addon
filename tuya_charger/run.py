{
  "name": "Tuya Charger MQTT",
  "version": "1.0.0",
  "slug": "tuya_charger",
  "description": "Interroga la colonnina Tuya e invia i dati via MQTT",
  "arch": ["amd64", "armv7", "armhf", "aarch64"],
  "startup": "application",
  "boot": "auto",
  "options": {
    "client_id": "",
    "client_secret": "",
    "device_id": "",
    "region": "tuyaeu",
    "poll_interval": 60,
    "mqtt_broker": "core-mosquitto",
    "mqtt_port": 1883,
    "mqtt_username": "",
    "mqtt_password": ""
  },
  "schema": {
    "client_id": "str",
    "client_secret": "str",
    "device_id": "str",
    "region": "str",
    "poll_interval": "int",
    "mqtt_broker": "str",
    "mqtt_port": "int",
    "mqtt_username": "str",
    "mqtt_password": "str"
  }
}
