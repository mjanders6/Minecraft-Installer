# Minecraft-Installer
Light bash script to create a Java Edition Minecraft Server 

# Install dependancies
- git
- build-essentials
- openjdk-21(or latest version)
- mcrcon repository: https://github.com/Tiiffi/mcrcon.git
- Optional: UFW Firewall to set firewall rules



# Running the Shell Code
1. First enabel the .sh files to be executable: chmod +X File-Name
2. Run the scripts with ./File-Name
3. Edit the eula.txt file: eula=true
4. Update the server.properties
-- rcon.port=25575
-- rcon.password=strong-password
-- enable-rcon=true
5. Add the minecraft.service file to the directory: /etc/systemd/system
6. Reload the daemon: sudo systemctl daemon-reload
7. Start the service: 
-- 

