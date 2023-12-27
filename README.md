# Preparation:
Make sure to have AWS CLI installed and update your AWS credentials.
Also, take your "labsuser.pem" key and replace the "labsuser.pem" key in the git repo. Do not commit and push the change. We only need your "labsuser.pem" key to SSH into instances and copy files. Ensure that your "labsuser.pem" key has the chmod 400 permissions.

 # Set up:
Navigate to the directory containing the Python files and run the following command:
-	`terraform init`
-	`terraform plan`
-	`terraform apply`

# Benchmark Standalone:
After setting up the standalone instance, copy the file `standalone.sh` and `standalone._setup.sh` to the standalone instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" standalone.sh ubuntu@Public_address_ip_of_standalone_instance:/home/ubuntu`
-	-	`scp -i "labsuser.pem" standalone_setup.sh ubuntu@Public_address_ip_of_standalone_instance:/home/ubuntu`
### On the standalone instance
After connecting to the instance, run the script with:
-	`chmod +x standalone_setup.sh`
-	`./standalone_setup.sh`
-	`chmod +x standalone.sh`
-	`./standalone.sh`.
  
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
After setting up the proxy instance, copy the files `proxy.py`and `proxy_setup.sh` y to the proxy instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" /LOG8415E/proxy.py ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
-	`scp -i "labsuser.pem" /LOG8415E/proxy_setup.sh ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
-		`scp -i "labsuser.pem" /LOG8415E/labsuser.pem ubuntu@Public_address_ip_of_proxy_instance:/home/ubuntu`
  
### On the Master instance
Run:
- `mysql -u root -p`
-	`CREATE USER 'usrname'@'proxy_public_ip' IDENTIFIED BY 'password';`
-	`GRANT ALL PRIVILEGES ON * . * TO 'usrname'@'proxy_public_ip';`
-	`FLUSH PRIVILEGES;`
### On the Proxy instance
Then, run :
- `chmod +x proxy_setup.sh`
- `./proxy_setup.sh`
 # gatekeeper:
After setting up the gatekeeper instance, copy the files `gatekeeper.py`and `gatekeeper_setup.sh` y to the gatekeeper instance using SCP and your access key. Run the script with the following commands:
To copy: 
-	`scp -i "labsuser.pem" /LOG8415E/gatekeeper.py ubuntu@Public_address_ip_of_gatekeeper_instance:/home/ubuntu`
-	`scp -i "labsuser.pem" /LOG8415E/gatekeeper_setup.sh ubuntu@Public_address_ip_of_gatekeeper_instance:/home/ubuntu`
### On the gatekeeper instance
Then, run :
- `chmod +x gatekeeper_setup.sh`
- `./gatekeeper_setup.sh`
 
