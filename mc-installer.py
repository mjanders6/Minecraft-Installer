# Developer: Mr. Anderson777
# Date: May 2024
# 
# Purpose: To automate building a Minecraft Server on an Ubuntu server. 
# 
# 
# Trouble shooting notes:
# - need to run as sudo 
# - need to install python3-pip
# - need to install inquirer as sudo
# 

import inquirer
from inquirer.themes import GreenPassion
from inquirer import errors, Password
import subprocess
from subprocess import STDOUT
import os
import shutil
import asyncio
from Class.setup import MC_Installer

MC_SETUP = MC_Installer()

# Global variables
GIT = 'git'
BUILD_Essential = 'build-essential'
OPENJDK = 'openjdk-21-jre-headless'
USERNAME = 'minecraft'

RCON_PORT = '25575'
RCON_ENABLE = 'true'
EULA = 'true'

# minecraft path
MC_PATH = '/opt/minecraft'
EULA_PATH = f'{MC_PATH}/server/eula.txt'
SERVER_PROPS_PATH = f'{MC_PATH}/server/server.properties'

# Paths for service file
src_pth = r"./minecraft.service"
dest_path=r"/etc/systemd/system/minecraft.service"

def run_options(input):
    match input:
        case 'Full':
            print('Run Full')
            full_qs = inquirer.prompt(full_resp)
            MC_SETUP.run_updates()
            MC_SETUP.run_upgrades()
            # Set password

            
            # Copy minecraft.service to the /etc/systemd/system location

            # Change password in the service file 

            # Create minecraft directories

            # Run installation

            print(full_qs)
        case 'Update':
            print('Update Jar file')
        case 'Uninstall':
            print('Remove everything')


# Set intall options
inst_options = inquirer.list_input(
    message="Choose which intallation option you woudl like:",
    choices=["Full", "Update", "Uninstall"],
)

full_resp = [
    # Create username
    inquirer.Text('username', 'Username. Change default name if you like. ', default='minecraft'),
    # Set password
    inquirer.Password('password', message='Please enter your password for mcron'),
    # Copy and paste link to minecraft jar file
    inquirer.Text('mc_jar', 'Copy and past the link to the most current jar file '),
]

run_options(inst_options)

