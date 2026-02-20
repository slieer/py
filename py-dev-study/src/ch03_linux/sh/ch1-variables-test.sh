#!/bin/bash
HELLO=Hello
function hello {
	local HELLO=World
	echo $HELLO 'slieer'
}

echo $HELLO
hello     #class hello()
echo $HELLO
