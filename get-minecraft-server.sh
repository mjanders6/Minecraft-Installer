#!/bin/bash

# Install Minecraft Server

#Might need to change this link based on the latest version
# https://www.minecraft.net/en-us/download/server
wget https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar -P ~/server

cd ~/server
java -Xmx1024M -Xms1024M -jar server.jar nogui


# Cange the eula.txt file 
# eula=true

# Update the server.properties
# This file can also be updated for a variety of configurations  
# rcon.port=25575
# rcon.password=SET-STRONG-PASSWORD
# enable-rcon=true