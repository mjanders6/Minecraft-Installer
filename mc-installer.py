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

# Global variables
GIT = 'git'
BUILD_Essential = 'build-essential'
OPENJDK = 'openjdk-21-jre-headless'

RCON_PORT = '25575'
RCON_ENABLE = 'true'

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


# Run the update/upgrade commands with no output 
proc = subprocess.Popen(f'sudo apt update && sudo apt upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
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
os.makedirs(os.path.expanduser('/opt/minecraft/{backups,tools,server}'), exist_ok=True)

# Download Minecraft server file
print("Downloading the Minecraft file: ")
mc_download = subprocess.run(["wget", "https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar", "-P", f'{MC_PATH}/server'])
mc_download.wait()

# Change directories and run Minecraft
print("Changing directories and running Minecraft. This will error out since it may be its first run.")
os.chdir(f'{MC_PATH}/server')
server_start = subprocess.run(["java", "-Xmx1024M", "-Xms1024M", "-jar", "server.jar", "nogui"])
server_start.wait()


# Update the eula.txt file
print("Going to update the eula.txt file now. Change false to true:")
with open(f'{EULA_PATH}', "r+") as f:
    content = f.read()
    content = content.replace("eula=false", "eula=true")
    f.seek(0)
    f.write(content)
    f.truncate()

# Update the server.properties file
print("Going to update the server.properties file:")
with open(f'{SERVER_PROPS_PATH}', "r+") as f:
    content = f.read()
    content = content.replace("rcon.port=", "rcon.port=" + RCON_PORT)
    content = content.replace("enable-rcon=", "enable-rcon=" + RCON_ENABLE)
    f.seek(0)
    f.write(content)
    f.truncate()


# choice = inquirer.list_input("Public or private?",
                              # choices=['public', 'private'])
# correct = inquirer.confirm("This will delete all your current labels and "
                        # "create a new ones. Continue?", default=False)
						
						