#!/bin/bash

# Make files executable
sudo chmod +x minecraft.sh get-minecraft-server.sh mcrcon-script.sh

# install applications. Might need to revise the versions
echo "Running updates and upgrades: "
sudo apt update -y
sudo apt upgrade -y
echo ""

# Open JDK 21 is one behind the most current version
sudo apt install -y git build-essential openjdk-21-jre-headless
echo ""

# Set rcon.password=SET-STRONG-PASSWORD
echo 'Enter the password you are going to use for rcon:'
read -s rcon_passwd
export rcon_passwd

# Add minecraft.service file
sudo cp minecraft.service /etc/systemd/system/minecraft.service

# Add password to the minecraft.service
sudo sed -i ''s/strong-password/$rcon_passwd/'' /etc/systemd/system/minecraft.service

# Install necessary applications and add minecraft user and directory
source minecraft.sh

# Get the minecraft server and start it
source get-minecraft-server.sh

# Setup mcrcon
source mcrcon-script.sh

# Restarting the daemon
sudo systemctl daemon-reload
sudo systemctl start minecraft
sudo systemctl enable minecraft

echo ""
echo "Do you want to reboot the server? y/n"
read ans_reboot

if [''$ans_reboot'' -eq 'y']; then
    echo "Going to reboot now"
    sudo reboot
else 
    echo ""
    echo "Ok, everything will work better after a good reboot."
    echo ""
fi
