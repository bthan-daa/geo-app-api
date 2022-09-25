# geo-app-api

This is intended for testing purposes for the Government of Ontario, LRC DAA Unit.

## Installation
To build the docker environment and app:

Run ```./run_vpn``` from the project directory if you are operating on a VPN or from the Government of Ontario ethernet

Run ```./run_novpn``` from the project directory if you are operating on a home/public network without a proxy.

Should you encounter any difficulties, please contact me.

## Usage

The above commands will build, migrate, and run the application. Should you want to close and clear the environment, run the following from the project directory:

```docker-compose down```

When you would like to restart the application (assuming it is already built), you can run the following from the project directory:

```docker-compose up```

