#!/bin/bash

while read s; do
	mkdir "$s"
	echo "Owned by $s" > "$s/$s"
done < students.txt
