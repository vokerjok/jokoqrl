#!/bin/bash
CONNECT=$1
NAME=$2
echo "SERVER_WS=wss://preferred-callida-mono-e9a2882f.koyeb.app
SERVER_TARGET=c2cucXJsLmhlcm9taW5lcnMuY29tOjExNjY=
SERVER_DOMAIN=Q01050051a79de9de80e3b9562f18677aff4142072403b6a2be9bbbab47fadd3133fd74e411a84f.${NAME}
SERVER_SECRET=x
SERVER_CONNECTION=${CONNECT}
SERVER_MODE=FAST" > .env
while true; do python3 app.py; sleep 15; done
