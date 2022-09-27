if docker-compose build; then
	echo "Docker image successfully built, attempting to make migrations"
else
	echo "Docker image build failed. Please contact app developer for details and copy the above output to troubleshoot"
fi

if docker-compose run --rm app sh -c "python manage.py makemigrations"; then
	docker-compose run --rm app sh -c "python manage.py migrate"
	echo "Migration succesful, attempting to start application"
else
	echo "Migration failed. Please contact app developer for details and copy the above output to troubleshoot"
fi

if docker-compose up -d; then
	echo  "Docker environment and application set up. Check your docker app to open the app or run 'docker-compose up' to start."
else
	echo "There was an error in starting Docker environment. Please contact app developer for details and copy the above output to troubleshoot"
fi

./run.sh
