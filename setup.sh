#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python 3.x and try again."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Activate the virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Install the required packages
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To activate the environment, run:"
echo "source env/bin/activate"

