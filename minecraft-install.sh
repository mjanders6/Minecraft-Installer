#!/bin/bash

# Make files executable
sudo chmod +x minecraft.sh get-minecraft-server.sh mcrcon-script.sh

# install applications. Might need to revise the versions
echo "Running updates and upgrades: "
sudo apt update -y
sudo apt upgrade -y
echo ""

# Open JDK 21 is one behind the most current version
applications = ["git", "build-essentials", "openjdk-21-jre-headless"]
sudo apt install -y "${applications[@]}"
echo ""

# Install necessary applications and add minecraft user and directory
source minecraft.sh

# Setup directories
echo "Setting up directories: "
sudo su - minecraft
mkdir -p ~/{backups,tools,server}
echo ""

# Get the minecraft server and start it
source get-minecraft-server.sh

# Setup mcrcon
source mcrcon-script.sh

# Add minecraft.service file
sudo cp minecraft.service /etc/systemd/system/minecraft.service

# Restarting the daemon
sudo systemctl daemon-reload
sudo systemctl start minecraft
sudo systemctl enable minecraft

echo ""
echo "Do you want to reboot the server? y/n"
read -s ans_reboot

if [''$ans_reboot'' -eq 'y']; then
    echo "Going to reboot now"
    sudo reboot
else 
    echo ""
    echo "Ok, everything will work better after a good reboot."
    echo ""
fi
