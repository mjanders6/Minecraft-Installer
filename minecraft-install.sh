#!/bin/bash

# Make all files executable
sudo chmod +x minecraft.sh get-minecraft-server.sh mcrcon-script.sh


# Install necessary applications and add minecraft user and directory
source minecraft.sh

# Get the minecraft server and start it
source get-minecraft-server.sh

# Setup mcrcon
source mcrcon-script.sh

