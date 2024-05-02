#!/bin/bash

echo "Setting up mcrcon: "
# Setup mcrcon
sudo -u minecraft bash << EOF
git clone https://github.com/Tiiffi/mcrcon.git ~/tools/mcrcon

cd ~/tools/mcrcon
gcc -std=gnu11 -pedantic -Wall -Wextra -O2 -s -o mcrcon mcrcon.c

echo ""
echo "mcrcon setup complete. "
echo ""

EOF