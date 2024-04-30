#!/bin/bash

# Setup Minecraft User
echo "adding the main minecraft user: "
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft
echo ""
