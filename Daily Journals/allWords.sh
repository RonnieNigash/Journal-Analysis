#!/bin/bash

# Remove spaces from filenames for easy process
for f in *\ *; do mv "$f" "${f// /_}"; done

# Append contest of *.html and *.rtf files to new file
for file in *.html *.rtf
do
	echo "Processing $file..."
	cat $file >> fileContents.txt
done
