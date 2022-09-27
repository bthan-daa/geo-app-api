if docker-compose up -d ; then
	echo "Docker container is now successfully running. Check the Docker app for more details."
else
	echo "There was an error with starting the Docker container. Please contact the developer with the logs."
fi
