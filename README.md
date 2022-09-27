# geo-app-api

This is intended for testing purposes for the Government of Ontario, LRC DAA Unit.

## Installation
To build the docker environment and app:

Run ```./build_vpn.sh``` from the project directory if you are operating on a VPN or from the Government of Ontario ethernet

Run ```./build_novpn.sh``` from the project directory if you are operating on a home/public network without a proxy.

Should you encounter any difficulties, please contact me.

## Usage

### Clearing Containers
The above commands will build, migrate, and run the application. Should you want to close and clear the environment, run the following from the project directory:

```docker-compose down```

### Starting Containers

When you would like to start the application (assuming it is already built), you can run the following from the project directory:

```./run.sh```

### Running commands within containers

Running python scripts within the container is handled through a shell script.

```./cmd.sh 'YOUR ARGUMENT HERE'```

#### Example usage

```./cmd.sh 'python manage.py migrations'```
```./cmd.sh 'python manage.py createsuperuser'```


