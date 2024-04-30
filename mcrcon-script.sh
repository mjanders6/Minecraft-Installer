#!/bin/bash

echo "Setting up mcrcon: "
# Setup mcrcon
git clone https://github.com/Tiiffi/mcrcon.git ~/tools/mcrcon

cd ~/tools/mcrcon
gcc -std=gnull -pedantic -Wall -Wextra -02 -s -o mcrcon mcrcon.c

echo ""
echo "mcrcon setup complete. "
echo ""