# Preparation:
Ensure that you have the following dependencies installed:
- Python 3
- boto3
- paramiko

Make sure to have AWS CLI installed and update your AWS credentials.

Also, take your "labsuser.pem" key and replace the "labsuser.pem" key in the git repo. Do not commit and push the change. We only need your "labsuser.pem" key to SSH into instances and copy files. Ensure that your "labsuser.pem" key has the chmod 400 permissions.

 # Set up:

Navigate to the directory containing the Python files and run the following command:
-	`python3 Main.py`

Ensure that you include the (172.31.16.0/20) subnet in the "Main.py" file on line 9. The script will manage the entire setup process, including security groups and instances.
# Benchmark Standalone:
After setting up the standalone instance, copy the file standalone.sh to the standalone instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" standalone.sh ubuntu@Public_address_ip_of_standalone_instance:/home/ubuntu`
### On the standalone instance
After connecting to the instance, run the script with:
-	`chmod +x standalone.sh`
-	`./standalone.sh`
Finally, find the result in the standaloneResult file.
# Benchmark Cluster:

After setting up the salves instances, copy the file slave.sh to each slave instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" /LOG8415E/slave.sh ubuntu@Public_address_ip_of_slave_instance:/home/ubuntu`
### On the Slave instance
After connecting to the instance, run the script with:
-	`chmod +x slave.sh`
-	`./slave.sh`
After setting up the master instance, copy the files cluster.sh and master.sh to master instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" /LOG8415E/master.sh ubuntu@Public_address_ip_of_master_instance:/home/ubuntu`
 -	`scp -i "labsuser.pem" /LOG8415E/cluster.sh ubuntu@Public_address_ip_of_master_instance:/home/ubuntu`
### On the Master instance
After connecting to the instance, run the script with:
-	`chmod +x master.sh`
-	`./master.sh`
-	`chmod +x cluster.sh`
-	`./cluster.sh`
Finally, find the result in the clusterResult file.
 # Proxy:
After setting up the proxy instance, copy the files proxy_Direct.py ,proxy_Random.py and proxy_customized.py to the proxy instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" /LOG8415E/proxy_Direct.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
-	`scp -i "labsuser.pem" /LOG8415E/proxy_Random.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
-	`scp -i "labsuser.pem" /LOG8415E/proxy_customized.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
### On the Master instance
Run:
-	`CREATE USER 'usrname'@'proxy_public_ip' IDENTIFIED BY 'password';`
-	`GRANT ALL PRIVILEGES ON * . * TO 'usrname'@'proxy_public_ip';`
### On the Proxy instance
Then, run the proxy:
-	`python3 proxy_Direct.py "Show tables" `
-	`python3 proxy_Random.py "Show tables"`
-	`python3 proxy_ customized.py "Show tables"`
