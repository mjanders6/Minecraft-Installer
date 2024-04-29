#!/bin/bash
echo "Running updates and upgrades: "
sudo apt update -y
sudo apt upgrade -y
echo ""

# install applications. Might need to revise the versions
# Open JDK 21 is one behind the most current version
applications = [git, build-essentials, openjdk-21-jre-headless]

# Setup Minecraft User
echo "adding the main minecraft user: "
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft
echo ""

# Setup directories
echo "Setting up directories: "
sudo su - minecraft
mkdir -p ~/{backups,tools,server}
echo ""
