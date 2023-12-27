# Update the package lists for upgrades and new package installations
sudo apt-get update

# Install Python3 and pip3
sudo apt-get install -y python3 python3-pip

# Install the Flask framework for Python3
sudo apt install -y python3-flask

# Install the Python3 virtual environment package
sudo apt install -y python3.10-venv

# Install the virtualenv package
pip3 install virtualenv

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Flask, requests, pymysql, pythonping, and sshtunnel Python libraries
sudo pip3 install flask requests pymysql pythonping sshtunnel


# Install Uncomplicated Firewall
sudo apt-get install -y ufw

# Install iptables-persistent
sudo apt install -y iptables-persistent

# Allow only necessary ports
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443

# Enable the firewall
sudo ufw enable

# This command adds a rule to the INPUT chain of the iptables firewall.
# It allows incoming TCP connections on ports 80 (HTTP) and 443 (HTTPS) that are either new or already established.
sudo iptables -A INPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# This command adds a rule to the OUTPUT chain of the iptables firewall.
# It allows outgoing TCP connections from ports 80 (HTTP) and 443 (HTTPS) that are already established.
sudo iptables -A OUTPUT -p tcp -m multiport --dports 80,443 -m conntrack --ctstate ESTABLISHED -j ACCEPT

# Save IP tables rules
sudo netfilter-persistent save

# Activate the virtual environment
source venv/bin/activate
# Run the gatekeeper.py script
sudo python3 gatekeeper.py