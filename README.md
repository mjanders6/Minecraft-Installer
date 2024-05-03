# Minecraft-Installer
Light python script to create a Java Edition Minecraft Server 

I have been using [How to Make Minecraft Server on Ubuntu 20.04](https://linuxize.com/post/how-to-make-minecraft-server-on-ubuntu-20-04/#configuring-backups) to make a solid Minecraft server. This also works for Ubuntu 22.04. I am essentially breaking up this instructions into a python script to automate the process. I will then test it out in an Ubuntu 22.04 VM to ensure it works properly. 

I initially crated bash scritps to automate the process. minecraft-install.sh is the script that can also be run to automate the process as well. 

# Install Dependencies
- git
- build-essentials
- openjdk-21(or latest version)
- mcrcon repository: `https://github.com/Tiiffi/mcrcon.git`
- Optional: UFW Firewall to set firewall rules
- Ensure `sed` is installed
- Inquirer and subprocess for the python script



# Running the Shell Code
1. Set `minecraft-install.sh` to an executable. It will set all necessary files as executable: `chmod +x File-Name`
2. Run `./minecraft-install.sh`
3. The `minecraft-install.sh` will perform the following:
	- Edit the eula.txt file: `eula=true`
	- Update the `server.properties`
		- `rcon.port=25575`
		- Prompt you to set the `rcon.password`
		- `enable-rcon=true`
	- Add the minecraft.service file to the directory: `/etc/systemd/system`
	- Reload the daemon: `daemon-reload`
	- Start the service: `sudo systemctl start minecraft`
	- Enable service to start after rebooting: `sudo systemctl enable minecraft`
	- Create script to backup the server file
4. Accessing the console
	- `/opt/minecraft/tools/mcrcon/mcrcon -H 127.0.0.1 -P 25575 -p strong-password -t`

# Running the Python Script
1. Run the script with 
	- `sudo python3 mc-installer.py`
2. Enter the password for mcrcon when prompted
3. When installation is complete, run the following to verify that everything worked:
	- `sudo systemctl status minecraft`

# Removing Minecraft
Note: This script will remove the minecraft user and its directory, remove the Minecraft-Installer directory, and re-clone the Minecraft-Installer repository.

1. Set the refresh.sh to an executable
2. Run `./refresh.sh`