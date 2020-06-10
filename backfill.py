from datetime import datetime
from dotenv import load_dotenv
from influxdb import InfluxDBClient
import os
import csv

load_dotenv()

def get_influx_client():
    return InfluxDBClient(
        os.environ.get("INFLUXDB_HOST"),
        int(os.environ.get("INFLUXDB_PORT")),
        os.environ.get("INFLUXDB_USER"),
        os.environ.get("INFLUXDB_PASSWORD"),
        os.environ.get("INFLUXDB_DATABASE"),
    )

def get_influx_payload(row):
    return [
        {
            "measurement": "router_connected",
            "time": row[0],
            "fields": {
                "value": int(row[1])
            }
        },
        {
            "measurement": "external_connected",
            "time": row[0],
            "fields": {
                "value": int(row[2])
            }
        }
    ]

def load_data():
    with open('data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        data = [r for r in reader if r[0] != "timestamp"]

    return data

if __name__ == '__main__':
    data = load_data()
    for row in data:
        get_influx_client().write_points(get_influx_payload(row))
