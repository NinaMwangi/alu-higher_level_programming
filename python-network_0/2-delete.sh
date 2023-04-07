#!/bin/bash
# Sends a delete request to url passed as the first arg and displays the body.
curl -sX DELETE "$1"
