#!/bin/bash

# Update package information
sudo apt-get update

# Install MySQL Server and sysbench
sudo apt install mysql-server sysbench -y

# Download and extract the Sakila sample database
wget https://downloads.mysql.com/docs/sakila-db.tar.gz
tar -xf sakila-db.tar.gz
rm sakila-db.tar.gz

# Execute SQL scripts to create Sakila database schema and populate data
sudo mysql -e "SOURCE sakila-db/sakila-schema.sql;"
sudo mysql -e "SOURCE sakila-db/sakila-data.sql;"

# Switch to the Sakila database for further use
sudo mysql -e "USE sakila;"
