#!/bin/bash

# Make all files executable
sudo chmod +x minecraft.sh get-minecraft-server.sh mcrcon-script.sh


# Install necessary applications and add minecraft user and directory
source minecraft.sh

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
