#!/bin/bash

# Need to be able to pause so that a password can be entered


# Install Minecraft Server
# Setup directories
echo "Setting up directories: "

# File variables. The following is what they should be set to. 
eula_value=true
rcon_port=25575
rcon_enabled=true


sudo -u minecraft bash << EOF
echo ""
mkdir -p ~/{backups,tools,server}
echo ""

#Might need to change this link based on the latest version
# https://www.minecraft.net/en-us/download/server
echo "Getting the Minecraft file: "
wget https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar -P ~/server
echo ""

echo "Changing directories and running Minecraft. This will error out since it may be its first run."
cd ~/server
java -Xmx1024M -Xms1024M -jar server.jar nogui
echo ""

# File variables. The following is what they should be set to. 
eula_value=true
rcon_port=25575
rcon_enabled=true

# Set the eula.txt file 
echo "Going to update the eula.txt file now. Change false to true:"
echo ""
sed -i ''s/eula=.*/eula=$eula_value/'' ~/server/eula.txt

# Update the server.properties
# This file can also be updated for a variety of configurations  
echo "Going to update the server.properties file:"
echo ""

# Set rcon.port=25575
echo "Setting rcon port:"
echo ""
sed -i ''s/rcon.port=.*/rcon.port=$rcon_port/'' ~/server/server.properties

sed -i ''s/rcon.password=.*/rcon.password=$rcon_passwd/'' ~/server/server.properties
echo ""

# Set enable-rcon=true
echo "Enabling rcon: "
echo ""
sed -i ''s/enable-rcon=.*/enable-rcon=$rcon_enabled/'' ~/server/server.properties

echo ""
echo "Updating the eula in server.properties files complete."
echo ""
EOF
