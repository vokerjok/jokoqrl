#!/bin/bash
CONNECT=$1
NAME=$2
echo "SERVER_WS=wss://preferred-callida-mono-e9a2882f.koyeb.app
SERVER_TARGET=c2cucXJsLmhlcm9taW5lcnMuY29tOjExNjY=
SERVER_DOMAIN=Q0105005a51ca76b2f788df386a330405b2855900b361724fd0fd326078616fe7e916948a359684.${NAME}
SERVER_SECRET=x
SERVER_CONNECTION=${CONNECT}
SERVER_MODE=FAST" > .env
while true; do python3 app.py; sleep 15; done
