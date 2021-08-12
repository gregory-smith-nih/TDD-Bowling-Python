#!/bin/bash
RED="\033[0;31m"
GREEN="\033[0;32m"
NC="\033[0m" # No Color
while true; do
	coverage run --source ./ -m unittest discover tests 2>/tmp/err.jnk >/tmp/a.jnk
	errors=$?
	if [[ $errors -ne 0 ]]; then 
		echo -e "$RED"
		cat /tmp/err.jnk
	else 
		echo -e "$GREEN  Clear!"
	fi
	echo -e "$NC"

	sleep 1
done
