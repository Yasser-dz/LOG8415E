#!/bin/bash

# Update package information
sudo apt update

# Install Python 3 and pip
sudo apt install python3-pip -y

# Install required Python packages
sudo pip install sshtunnel  # Install sshtunnel for SSH tunneling
sudo pip install pythonping  # Install pythonping for ICMP ping functionality
sudo pip install pymysql  # Install pymysql for MySQL database connections
