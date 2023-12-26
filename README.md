# Preparation:
Ensure that you have the following dependencies installed:
- Python 3
- boto3
- paramiko

Make sure to have AWS CLI installed and update your AWS credentials.

Also, take your "labsuser.pem" key and replace the "labsuser.pem" key in the git repo. Do not commit and push the change. We only need your "labsuser.pem" key to SSH into instances and copy files. Ensure that your "labsuser.pem" key has the chmod 400 permissions.

 # Set up:

Navigate to the directory containing the Python files and run the following command:
1 -	`python3 Main.py`

Ensure that you include the (172.31.16.0/20) subnet in the "Main.py" file on line 9. The script will manage the entire setup process, including security groups and instances.
# Benchmark Standalone:
After setting up the standalone instance, copy the file standalone.sh to the standalone instance using SCP and your access key. Run the script with the following commands:
To copy: 
1-	`scp -i "labsuser.pem" standalone.sh ubuntu@Public_address_ip_of_standalone_instance:/home/ubuntu`
### On the standalone instance
After connecting to the instance, run the script with:
1-	chmod +x standalone.sh
2-	./standalone.sh
Finally, find the result in the standaloneResult file.
#Benchmark Cluster:
After setting up the salves instances, copy the file slave.sh to each slave instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	scp -i "labsuser.pem" /LOG8415E/slave.sh ubuntu@Public_address_ip_of_slave_instance:/home/ubuntu
### On the Slave instance
After connecting to the instance, run the script with:
1-	chmod +x slave.sh
2-	./slave.sh
After setting up the master instance, copy the files cluster.sh and master.sh to master instance using SCP and your access key. Run the script with the following commands:
To copy: 
1 -	scp -i "labsuser.pem" /LOG8415E/master.sh ubuntu@Public_address_ip_of_master_instance:/home/ubuntu
2 -	scp -i "labsuser.pem" /LOG8415E/cluster.sh ubuntu@Public_address_ip_of_master_instance:/home/ubuntu
### On the Master instance
After connecting to the instance, run the script with:
1 -	chmod +x master.sh
2 -	./master.sh
3 -	chmod +x cluster.sh
4 -	./cluster.sh
Finally, find the result in the clusterResult file.
 # Proxy:
After setting up the proxy instance, copy the files proxy_Direct.py ,proxy_Random.py and proxy_customized.py to the proxy instance using SCP and your access key. Run the script with the following commands:
To copy: 
1 -	scp -i "labsuser.pem" /LOG8415E/proxy_Direct.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu
2 -	scp -i "labsuser.pem" /LOG8415E/proxy_Random.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu
3 -	scp -i "labsuser.pem" /LOG8415E/proxy_customized.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu
### On the Master instance
1-	CREATE USER 'usrname'@'proxy_public_ip' IDENTIFIED BY 'password';
2-	GRANT ALL PRIVILEGES ON * . * TO 'usrname'@'proxy_public_ip';
### On the Proxy instance
Then, run the proxy:
1 -	python3 proxy_Direct.py "Show tables" 
2 -	python3 proxy_Random.py "Show tables"
3 -	python3 proxy_ customized.py "Show tables"
