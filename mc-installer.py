# Developer: Mr. Anderson777
# Date: May 2024
# 
# Purpose: To automate building, updating, and removing a Minecraft Server on an Ubuntu server. 
# 
# 
# 

import inquirer
from Class.setup import MC_Installer

MC_SETUP = MC_Installer()

# Global variables
GIT = 'git'
BUILD_Essential = 'build-essential'
OPENJDK = 'openjdk-21-jre-headless'

# Paths for service file
src_pth = r"./minecraft.service"
dest_path=r"/etc/systemd/system/minecraft.service"

def run_options(input):
    match input:
        case 'Full':
            print('Run Full installation')
            full_qs = inquirer.prompt(full_resp)
            MC_SETUP.run_updates()
            MC_SETUP.run_upgrades()
            MC_SETUP.inst_dependancies(GIT, BUILD_Essential, OPENJDK)
            # Copy minecraft.service to the /etc/systemd/system location
            # Change password in the service file 
            MC_SETUP.mc_service(src_pth, dest_path, full_qs['password'])
            # Create minecraft directories
            #MC_SETUP.set_dirs(full_qs['username'])
            MC_SETUP.set_dirs()
            # Run installation
            #MC_SETUP.mc_install(full_qs['username'], full_qs['mc_jar'], full_qs['password'])
            MC_SETUP.mc_install(full_qs['mc_jar'], full_qs['password'])
            print(full_qs)
        case 'Update':
            print('Update Jar file')
            update_qs = inquirer.prompt(mc_update_pt)
            MC_SETUP.mc_update(update_qs['username'], update_qs['mc_jar'])
        case 'Uninstall':
            print('Remove everything')
            uname = inquirer.text('Enter the name used to install minecraft: The default is `minecraft`. \nIf you can remember the name may be found in the /opt directory.', default='minecraft')
            MC_SETUP.mc_uninstall(uname)


# Set intall options
inst_options = inquirer.list_input(
    message="Choose which intallation option you woudl like:",
    choices=["Full", "Update", "Uninstall"],
)

# Full install prompt variables
full_resp = [
    # Create username
    inquirer.Text('username', 'Username. Change default name if you like. ', default='minecraft'),
    # Set password
    inquirer.Password('password', message='Please enter your password for mcron'),
    # Copy and paste link to minecraft jar file
    inquirer.Text('mc_jar', 'Copy and past the link to the most current jar file '),
]

# Update prompt vriables
mc_update_pt = [
    # Create username
    inquirer.Text('username', 'Enter the username that was used during installation. If the default was used, keep this default. ', default='minecraft'),
    # Copy and paste link to minecraft jar file
    inquirer.Text('mc_jar', 'Copy and past the link to the most current jar file '),
]

run_options(inst_options)

