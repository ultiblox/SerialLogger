#!/bin/bash

# Exit on error
set -e

# Set the system-wide installation directory for Arduino CLI
BINDIR="/usr/local/bin"
CLI_VERSION="latest"  # Change to a specific version if needed

# Check if Arduino CLI is already installed
if command -v arduino-cli &> /dev/null; then
    echo "Arduino CLI is already installed."
else
    echo "Installing Arduino CLI system-wide to $BINDIR..."

    # Download and install Arduino CLI with sudo permissions
    curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sudo BINDIR=$BINDIR sh -s $CLI_VERSION

    # Check if the installation was successful
    if [ $? -ne 0 ]; then
        echo "Error: Arduino CLI installation failed."
        exit 1
    else
        echo "Arduino CLI installed successfully in $BINDIR."
    fi
fi

# Verify the Arduino CLI installation
arduino-cli version

# Install Python dependencies
echo "Updating pip..."
pip install --upgrade pip

echo "Installing SerialLoggerHandler module..."
pip install git+ssh://git@github.com/ultiblox/SerialLoggerHandler.git

echo "Setup complete. The environment is ready!"

