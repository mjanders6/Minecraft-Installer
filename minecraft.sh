#!/bin/bash

# Setup Minecraft User
echo "adding the main minecraft user: "
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft
echo ""

# Setup directories
echo "Setting up directories: "
sudo su - minecraft
mkdir -p ~/{backups,tools,server}
echo ""
