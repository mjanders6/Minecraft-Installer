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
import subprocess
from subprocess import STDOUT
import os
import shutil
import asyncio
from Class.setup import MC_Installer


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

# Funcations 
def alter_file(file_path, old_word, new_word):
    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Replace the old word with the new word
    modified_content = file_content.replace(old_word, new_word)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

def switch_user(username):
    try:
        # Execute the command 'sudo su - username' using subprocess
        subprocess.run(['sudo', 'su', '-', username], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_commands_as_user(username, commands):
    try:
        # Execute commands as the new user
        subprocess.run(['sudo', '-u', username, *commands], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        
# Run the update/upgrade commands with no output 
proc = subprocess.Popen('sudo apt update && sudo apt upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
print("Running updates and insstalling necessary packages.")
proc.wait()
print("")

# Install dependancies
install_dependancies = subprocess.Popen(f'sudo apt install {GIT} {BUILD_Essential} {OPENJDK}', shell=True, stdin=None)
install_dependancies.wait()
print("")

# Set password
password = inquirer.password(message='Please enter your password for mcron: ')

# Copy minecraft.service to the /etc/systemd/system location
shutil.copyfile(src_pth, dest_path)


# Change password in the service file 
alter_file(dest_path, "strong-password", password)

# Create minecraft directories
create_user = subprocess.run(["sudo", "useradd", "-r", "-m", "-U", "-d", "/opt/minecraft", "-s", "/bin/bash", "minecraft"])
os.makedirs(os.path.expanduser('/opt/minecraft/backups'), exist_ok=True)
os.makedirs(os.path.expanduser('/opt/minecraft/server'), exist_ok=True)
os.makedirs(os.path.expanduser('/opt/minecraft/tools'), exist_ok=True)
subprocess.run(['sudo', 'chown', '-R', f'{USERNAME}:{USERNAME}', MC_PATH], check=True)

first_commands = [
    print('\n Downloading Minecraft server from the Minecraft website: \n'),
    subprocess.Popen('wget https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar -P /opt/minecraft/server', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    os.chdir('/opt/minecraft/server'),
    print('Initializing Minecraft. Going to fail since the eula.txt is set to false. Be patient, this will take some time. Dont stop the process. \n'),
    subprocess.Popen('java -Xmx1024M -Xms1024M -jar server.jar nogui', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Setting the eula.txt to true. \n'),
    subprocess.Popen('sed -i 'f's/eula=.*/eula={EULA}/'' /opt/minecraft/server/eula.txt', shell=True, stdin=None),
    print('Changing the rcon port. \n'),
    subprocess.Popen('sed -i 'f's/rcon.port=.*/rcon.port={RCON_PORT}/'' /opt/minecraft/server/server.properties', shell=True, stdin=None),
    print('Enable rcon. \n'),
    subprocess.Popen('sed -i 'f's/enable-rcon=.*/enable-rcon={RCON_ENABLE}/'' /opt/minecraft/server/server.properties', shell=True, stdin=None),
    print('Adding the password to rcon. \n'),
    subprocess.Popen('sed -i 'f's/rcon.password=.*/rcon.password={password}/'' /opt/minecraft/server/server.properties', shell=True, stdin=None),
    print('Downloading mcrcon from the git repository. \n'),
    subprocess.Popen('git clone https://github.com/Tiiffi/mcrcon.git /opt/minecraft/tools/mcrcon', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Changing directory to mcrcon. \n'),
    os.chdir('/opt/minecraft/tools/mcrcon'),
    print('Initializing mcrcon. \n'),
    subprocess.Popen('gcc -std=gnu11 -pedantic -Wall -Wextra -O2 -s -o mcrcon mcrcon.c', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Setting the minecraft directory. \n'),
    subprocess.Popen(f'sudo chown -R {USERNAME}:{USERNAME} {MC_PATH}', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Reloading deamon. \n'),
    subprocess.Popen('sudo systemctl daemon-reload', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Starting Minecraft. \n'),
    subprocess.Popen('sudo systemctl start minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Enabling Minecraft to start upon rebooting the server. \n'),
    subprocess.Popen('sudo systemctl enable minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
    print('Installation complete. Give it a minute to run through its processes and run: \n '' sydo systemctl status minecraft'' \n'),
]

run_commands_as_user(USERNAME, first_commands)