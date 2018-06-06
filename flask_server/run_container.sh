#!/bin/bash

PORTS="5000:5000"

docker run -it -p $PORTS -v $(pwd)/requirements.txt:/requirements.txt $1 flask_server
