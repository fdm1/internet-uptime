from datetime import datetime
from dotenv import load_dotenv
from influxdb import InfluxDBClient
import os

load_dotenv()

def get_influx_client():
    return InfluxDBClient(
        os.environ.get("INFLUXDB_HOST"),
        int(os.environ.get("INFLUXDB_PORT")),
        os.environ.get("INFLUXDB_USER"),
        os.environ.get("INFLUXDB_PASSWORD"),
        os.environ.get("INFLUXDB_DATABASE"),
    )

def get_influx_payload():
    return [
        {
            "measurement": "router_connected",
            "fields": {
                "value": check_ping(os.environ.get("ROUTER_HOST"))
            }
        },
        {
            "measurement": "external_connected",
            "fields": {
                "value": check_ping(os.environ.get("EXTERNAL_HOST"))
            }
        }
    ]

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    return 1 if response == 0 else 0

def log_connection():
    get_influx_client().write_points(get_influx_payload())


if __name__ == '__main__':
    log_connection()
