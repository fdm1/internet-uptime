#! /bin/bash

set -eu -o pipefail

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker run --rm -v $SCRIPT_DIR:/app -w /app python python check_connection.py
