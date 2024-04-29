# Minecraft-Installer
Light bash script to create a Java Edition Minecraft Server 

I have been using [How to Make Minecraft Server on Ubuntu 20.04](https://linuxize.com/post/how-to-make-minecraft-server-on-ubuntu-20-04/#configuring-backups) to make a solid Minecraft server. This also works for Ubuntu 22.04. I am essentially breaking up this instructions into executable bash scripts to automate the process. I will then test it out in an Ubuntu 22.04 VM to ensure it works properly. 

# Install Dependencies
- git
- build-essentials
- openjdk-21(or latest version)
- mcrcon repository: `https://github.com/Tiiffi/mcrcon.git`
- Optional: UFW Firewall to set firewall rules
- Ensure `sed` is installed



# Running the Shell Code
1. Set `minecraft-install.sh` to an executable. It will set necessary files as executable: `chmod +x File-Name`
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
