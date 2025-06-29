# tuya-charger-addon
# Tuya Charger MQTT Add-on

Legge i dati da una colonnina Tuya e li invia via MQTT.

## Configurazione

Inserisci in `config.json` i valori:
- `client_id`, `client_secret`, `device_id`, `region`
- `mqtt_broker`, `mqtt_port`, `mqtt_username/password`

## Installazione

1. Crea cartella `tuya_charger` in `/addons/local/`
2. Copia i file dentro (Dockerfile, config.json, run.py, README.md)
3. In Home Assistant → Supervisor → Add‑on Store → tre puntini → Re‑load add‑on store
4. Installa e configura l’add-on
5. Avvia l’add‑on: inizierà ad inviare dati MQTT su `tuya/charger/<device_id>/<sensor_code>`

## Utilizzo in Home Assistant

Aggiungi in `configuration.yaml`:

```yaml
sensor:
  - platform: mqtt
    name: "Corrente Colonnina"
    state_topic: "tuya/charger/<device_id>/current"
    unit_of_measurement: "A"
