#!/usr/bin/python3
#Printing the ASCII alphabet in lowercase, not followed by a new line.
for l in range(97, 123):
    if chr(l) is not 'q' and chr(l) is not 'e':
        print("{}".format(chr(l)), end="")
