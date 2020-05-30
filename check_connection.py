from datetime import datetime
import csv
import os

ROUTER_HOST = '192.168.0.1'
EXTERNAL_HOST = 'google.com'
DATA_FILE = 'data.csv'
HEADERS = ["timestamp", "router_connected", "external_connected"]


def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    return response == 0

def create_data_file_if_not_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(HEADERS)

def log_connection():
    row = [
        datetime.now().isoformat(),
        check_ping(ROUTER_HOST),
        check_ping(EXTERNAL_HOST)
    ]

    with open(DATA_FILE, "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


if __name__ == '__main__':
    create_data_file_if_not_exists()
    log_connection()

