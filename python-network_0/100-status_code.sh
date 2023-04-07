#!/bin/bash
# sends request to URL as an arg and displays only the status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
