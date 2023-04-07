#!/bin/bash
# A script that sends a JSON POST request to a URL & displays the body.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
