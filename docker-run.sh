#! /bin/bash

set -eu -o pipefail

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPT_DIR
pipenv lock --requirements > requirements.txt
docker build -t internet_uptime .

docker run --rm -v $SCRIPT_DIR:/app -w /app --network influxdb internet_uptime
