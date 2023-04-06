#!/bin/bash

# Takes in a URL, send a request to the URL, the displays the size of the body.
curl -s "$1" | wc -c
