# Minecraft-Installer
Light python script to create a Java Edition Minecraft Server 

I have been using [How to Make Minecraft Server on Ubuntu 20.04](https://linuxize.com/post/how-to-make-minecraft-server-on-ubuntu-20-04/#configuring-backups) to make a solid Minecraft server. This also works for Ubuntu 22.04. I am essentially breaking up this instructions into a python script to automate the process. I will then test it out in an Ubuntu 22.04 VM to ensure it works properly. 

I initially crated bash scripts to automate the process. This can be found in [Minecraft-Installer---Bash-Scripts](https://github.com/mjanders6/Minecraft-Installer---Bash-Scripts.git). 

# Minecraft Jar files: 
- [1.20.5](https://piston-data.mojang.com/v1/objects/79493072f65e17243fd36a699c9a96b4381feb91/server.jar)
- [1.20.6](https://piston-data.mojang.com/v1/objects/145ff0858209bcfc164859ba735d4199aafa1eea/server.jar)
- [1.21.0](https://piston-data.mojang.com/v1/objects/450698d1863ab5180c25d7c804ef0fe6369dd1ba/server.jar)

# Dependencies
## To be Installed during installation 
- git
- build-essentials
- openjdk-21(or latest version)
- mcrcon repository: `https://github.com/Tiiffi/mcrcon.git`
- Optional: UFW Firewall to set firewall rules

## Required prior to running the script 
- Ensure `sed` is installed
- Inquirer and subprocess for the python script

# Running the Python Script
1. Run the script with 
	- `sudo python3 mc-installer.py`
2. Enter the password for mcrcon when prompted
3. Paste in the link to the Minecraft Jar file.
4. When installation is complete, run the following to verify that everything worked:
	- `sudo systemctl status minecraft`

# Un-install Minecraft
1. Run the script with 
	- `sudo python3 mc-installer.py`
	- Select `Uninstall`
	- Enter the name of the minecraft server. If the default was left during installation, leave the default name during this process.

# Accessing the console
1. `/opt/minecraft/tools/mcrcon/mcrcon -H 127.0.0.1 -P 25575 -p strong-password -t`

