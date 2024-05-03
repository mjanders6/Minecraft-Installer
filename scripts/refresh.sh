#!/bin/bash

sudo systemctl stop minecraft

pid=`pgrep -u minecraft`
sudo kill -9 $pid

sudo userdel minecraft

sudo rm -rf Minecraft-Installer /opt/minecraft /etc/systemd/system/minecraft.service

git clone https://github.com/mjanders6/Minecraft-Installer.git

cd ~/Minecraft-Installer

sudo systemctl daemon-reload
