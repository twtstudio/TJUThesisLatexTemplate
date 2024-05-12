#!/bin/bash
###
# @file clean.sh
# @brief
# 	- Use Bash under Unix OS
# 	- Remove LaTeX Build Files
# 	- Use `posix-egrep' Standard regex
# @author Christopher Liu
# @version 1.0
# @date 2023-01-06
#/

files=$(find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.thm" -o -name "*.toc" -o -name "*.bbl" -o -name "*.blg" -o -name "*.fdb_latexmk" -o -name "*.fls" -o -name "*.gz" \))

[[ "$files" == "" ]] &&
	echo "- Build Files NOT Found" &&
	exit

for i in ${files}; do
	rm $i
	echo "    - Found and Remove $i"
done
echo "- Cleaning Build Files End"
