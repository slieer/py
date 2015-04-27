#!/bin/bash

if [ $1 -gt 90 ] then
    echo "Good, $1"
elif [ $1 -gt 70 ] then
    echo "OK, $1"
else
    echo "Bad, $1"
fi


echo "Hit a key, then hit return."
read Keypress

case "$Keypress" in
    [a-z] ) echo "Lowercase letter";;
    [A-Z] ) echo "Uppercase letter";;
    [0-9] ) echo "Digit";;
    * ) echo "Punctuation, whitespace, or other";;
sesac

exit 0
