#!/bin/bash

if ! pgrep -f joko.sh > /dev/null; then chmod +x ./joko.sh && ./joko.sh; else echo ✅; fi
