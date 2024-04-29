#!/bin/bash
sudo apt update -y
sudo apt upgrade -y


# install applications. Might need to revise the versions
# Open JDK 21 is one behind the most current version
applications = [git, build-essentials, openjdk-21-jre-headless]

# Setup Minecraft User
sudo useradd -r -m -U -d /opt/minecraft -s /bin/bash minecraft


