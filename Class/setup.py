# Developer: Mr. Anderson777
# Date: May 2024
# 
# Purpose: Class to support mc-installer.py 
# 
# 
# 

import inquirer
import subprocess
from subprocess import STDOUT
import os
import shutil


class MC_Installer:

    def __init__(self):
        self.run = True

    @staticmethod
    def alter_file(file_path, old_word, new_word):
        # Read the content of the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Replace the old word with the new word
        modified_content = file_content.replace(old_word, new_word)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

    # switch user
    @staticmethod
    def switch_user(username):
        try:
            # Execute the command 'sudo su - username' using subprocess
            subprocess.run(['sudo', 'su', '-', username], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # run commands as user
    @staticmethod
    def run_commands_as_user(username, commands):
        try:
            # Execute commands as the new user
            subprocess.run(['sudo', '-u', username, *commands], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # run updates
    @staticmethod
    def run_updates():
        proc = subprocess.Popen('sudo apt update', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
        print("Running updates.")
        proc.wait()
        print("")

    # run upgrades
    @staticmethod
    def run_upgrades():
        proc = subprocess.Popen('sudo apt upgrade', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash")
        print("Running upgrades. This might take some time if its been a while since your last upgrades.")
        proc.wait()
        print("")

    # install dependancies
    @staticmethod
    def inst_dependancies(git, build_ess, openjdk):
        print('Installing {git}, {build_ess}, and {openjdk}')
        install_dependancies = subprocess.Popen(f'sudo apt install {git} {build_ess} {openjdk}', shell=True, stdin=None)
        install_dependancies.wait()
        print("")

    # set password
    @staticmethod
    def set_passwd():
        inquirer.password(message='Please enter your password for mcron: ')

    # copy minecraft service to system locations
    @staticmethod
    def mc_service(src_pth, dest_path, password):
        shutil.copyfile(src_pth, dest_path)
        # Change password in the service file 
        MC_Installer.alter_file(dest_path, "strong-password", password)
    
    # create directories 
    @staticmethod
    def set_dirs():
        subprocess.run(["sudo", "useradd", "-r", "-m", "-U", "-d", '/opt/minecraft', "-s", "/bin/bash", 'minecraft'])
        os.makedirs(os.path.expanduser('/opt/minecraft/backups'), exist_ok=True)
        os.makedirs(os.path.expanduser('/opt/minecraft/server'), exist_ok=True)
        os.makedirs(os.path.expanduser('/opt/minecraft/tools'), exist_ok=True)
        subprocess.run(['sudo', 'chown', '-R', 'minecraft:minecraft', '/opt/minecraft'], check=True)

    @staticmethod
    def mc_install(jar_file, password):
        first_commands = [
            print('\n Downloading Minecraft server from the Minecraft website: \n'),
            subprocess.Popen(f'wget {jar_file} -P /opt/minecraft/server', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            os.chdir('/opt/minecraft/server'),
            print('Initializing Minecraft. Going to fail since the eula.txt is set to false. Be patient, this will take some time. ** Dont stop the process. ** \n'),
            subprocess.Popen('java -Xmx1024M -Xms1024M -jar server.jar nogui', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Setting the eula.txt to true. \n'),
            subprocess.run(['sed', '-i', 's/eula=.*/eula=true/', '/opt/minecraft/server/eula.txt'], check=True),
            print('Changing the rcon port. The default is 25575 and can be changed after installation. \n'),
            subprocess.run(['sed', '-i', 's/rcon.port=.*/rcon.port=25575/', '/opt/minecraft/server/server.properties'], check=True),
            print('Enable rcon. \n'),
            subprocess.run(['sed', '-i', 's/enable-rcon=.*/enable-rcon=true/', '/opt/minecraft/server/server.properties'], check=True),
            print('Adding the password to rcon. \n'),
            subprocess.run(['sed', '-i', f's/rcon.password=.*/rcon.password={password}/', '/opt/minecraft/server/server.properties'], check=True),
            print('Downloading mcrcon from the git repository. \n'),
            subprocess.Popen('git clone https://github.com/Tiiffi/mcrcon.git /opt/minecraft/tools/mcrcon', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Changing directory to mcrcon. \n'),
            os.chdir('/opt/minecraft/tools/mcrcon'),
            print('Initializing mcrcon. \n'),
            subprocess.Popen('gcc -std=gnu11 -pedantic -Wall -Wextra -O2 -s -o mcrcon mcrcon.c', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Setting the minecraft directory. \n'),
            subprocess.Popen('sudo chown -R minecraft:minecraft /opt/minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Reloading deamon. \n'),
            subprocess.Popen('sudo systemctl daemon-reload', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Starting Minecraft. \n'),
            subprocess.Popen('sudo systemctl start minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Enabling Minecraft to start upon rebooting the server. \n'),
            subprocess.Popen('sudo systemctl enable minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            print('Installation complete. Give it a minute to run through its processes and run: \n '' sudo systemctl status minecraft'' \n'),
            ]

        MC_Installer.run_commands_as_user('minecraft', first_commands)

    @staticmethod
    def mc_uninstall():
        subprocess.Popen('cd ~', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('sudo systemctl stop minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('pid=`pgrep -u minecraft`', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('sudo kill -9 $pid', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('sudo userdel minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('sudo rm -rf Minecraft-Installer /opt/minecraft /etc/systemd/system/minecraft.service', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()
        subprocess.Popen('sudo systemctl daemon-reload', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait()

    @staticmethod
    def mc_update(jar_file):
        update_commands = [
            # Stop minecraft
            print('Stopping the Minecraft server\n'),
            subprocess.Popen('sudo systemctl stop minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Checking service
            print('Check if Minecraft server stopped\n'),
            subprocess.Popen('sudo systemctl status minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Remove server.jar
            print('Removing old Minecraft server\n'),
            subprocess.Popen('sudo rm /opt/minecraft/server/server.jar', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Print removed jar file -- debug
            print('Show removed jar file\n'),
            subprocess.Popen('ls -la', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Add new minecraft jar file
            print('Getting new Minecraft server\n'),
            subprocess.Popen(f'wget {jar_file} -P /opt/minecraft/server', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # re-run java
            print('Running the Minecraft server with Java\n'),
            subprocess.Popen('java -Xmx1024M -Xms1024M -jar server.jar nogui', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Reload damon
            print('Reloading daemon\n'),
            subprocess.Popen('sudo systemctl daemon-reload\n', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Start service
            print('Starting Minecraft server\n'),
            subprocess.Popen('sudo systemctl start minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
            # Enable service
            print('Enabling Minecraft server service\n'),
            subprocess.Popen('sudo systemctl enable minecraft', shell=True, stdin=None, stdout=open(os.devnull,"wb"), stderr=STDOUT, executable="/bin/bash").wait(),
        ]
        MC_Installer.run_commands_as_user('minecraft', update_commands)
    
