#!/bin/bash
#Takes in a URL, sends POST to passed URL & displays body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
