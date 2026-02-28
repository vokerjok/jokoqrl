#!/bin/bash

APP_DIR="$(pwd)/app"
THREADS=8
NAME="joko-2c"

while true
do
    echo "[INFO] Starting run.sh..."

    cd "$APP_DIR" || exit 1
    chmod 777 run.sh

    echo "[INFO] CPU Core: $(nproc --all)"
    
    ./run.sh $THREADS $NAME >/dev/null 2>&1

    echo "[WARN] run.sh stopped! Restarting in 5 seconds..."
    sleep 5
done
