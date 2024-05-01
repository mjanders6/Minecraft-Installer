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

# Paths for service file
src_pth = r"./minecraft.service"
dest_path=r"/etc/systemd/system/minecraft.service"


# Run the commands with no output 
proc = subprocess.Popen(f'sudo apt upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
# Run updates and upgrades
#proc = subprocess.Popen('sudo apt update && sudo apt upgrade', shell=True, stdin=None)
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

def alter_file(file_path, old_word, new_word):
    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Replace the old word with the new word
    modified_content = file_content.replace(old_word, new_word)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Change password in the service file 
alter_file(dest_path, "strong-password", password)


# choice = inquirer.list_input("Public or private?",
                              # choices=['public', 'private'])
# correct = inquirer.confirm("This will delete all your current labels and "
                        # "create a new ones. Continue?", default=False)
						
						