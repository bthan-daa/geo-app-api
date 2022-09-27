#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "usage: ./cmd.sh 'YOUR ARGUMENT HERE'"
else
	docker-compose run --rm app sh -c "$1"
fi

