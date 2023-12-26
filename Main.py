import sys
import time
import boto3
import paramiko
import subprocess
from instances import *  # Import functions from instances.py
from securityGroup import *  # Import functions from securityGroup.py

subnet_id = 'subnet-0e9058cb01bac003f' # Changer Your Subnet Make sure to put the (172.31.16.0/20) subnet  

def main():

### Standalone 

    # Create AWS EC2 clients and resources
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    ec2_resource = boto3.resource("ec2", region_name="us-east-1")
    
    
    #get vpc_id
    vpc_id = ec2_client.describe_vpcs().get('Vpcs', [{}])[0].get('VpcId', '')
     # create security group
    security_group = create_standalone_security_group(ec2_client,"standalone_group",vpc_id)
    
    time.sleep(10)

    # # Create standalone EC2 instance
    instance = create_standalone_instance(ec2_resource, security_group['GroupId'], subnet_id)

    print("Waiting for standalone instance to be ok...")
    waiter = ec2_client.get_waiter('instance_status_ok')
    waiter.wait(InstanceIds=[instance[0].id])
    time.sleep(180)
    print("Standalone instance created successfully ...!")

    ## Cluster 
     
    # Create AWS EC2 clients and resources
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    ec2_resource = boto3.resource("ec2", region_name="us-east-1")
    
    #get vpc_id
    vpc_id = ec2_client.describe_vpcs().get('Vpcs', [{}])[0].get('VpcId', '')
     # create security group
    security_group = create_cluster_security_group(ec2_client,"cluster_group",vpc_id)
    
    time.sleep(10)

## Create cluster
    master = create_cluster_instance(ec2_resource, "172.31.17.2", security_group['GroupId'], open('master.sh').read(), "Master", subnet_id)
    slave_1 = create_cluster_instance(ec2_resource, "172.31.17.3", security_group['GroupId'], open('slave.sh').read(), "Slave-1", subnet_id)
    slave_2 = create_cluster_instance(ec2_resource, "172.31.17.4", security_group['GroupId'], open('slave.sh').read(), "Slave-2", subnet_id)
    slave_3 = create_cluster_instance(ec2_resource, "172.31.17.5", security_group['GroupId'], open('slave.sh').read(), "Slave-3", subnet_id)

    print("Waiting for cluster instances to be ok...")
    waiter = ec2_client.get_waiter('instance_status_ok')
    waiter.wait(InstanceIds=[master[0].id])
    waiter.wait(InstanceIds=[slave_1[0].id])
    waiter.wait(InstanceIds=[slave_2[0].id])
    waiter.wait(InstanceIds=[slave_3[0].id])
     
    time.sleep(180)
    print("Cluster instances created successfully ...!")

### Proxy
    
    # Create AWS EC2 clients and resources
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    ec2_resource = boto3.resource("ec2", region_name="us-east-1")
    
    
    #get vpc_id
    vpc_id = ec2_client.describe_vpcs().get('Vpcs', [{}])[0].get('VpcId', '')

     # create security group
    security_group = create_proxy_security_group(ec2_client,"proxy_group",vpc_id)
    
    time.sleep(10)

    # Create EC2 instance
    instance = create_proxy_instance(ec2_resource, "172.31.17.6", security_group['GroupId'], subnet_id)

    print("Waiting for the proxy instance to be ok...")
    waiter = ec2_client.get_waiter('instance_status_ok')
    waiter.wait(InstanceIds=[instance[0].id])
    # Get public IP
    reservations = ec2_client.describe_instances(InstanceIds=[instance[0].id])['Reservations']
    ip = reservations[0]["Instances"][0].get('PublicIpAddress')

    print("SCP the labsuser.pem to the proxy...")
    subprocess.call(['scp', '-o','StrictHostKeyChecking=no', '-o', 'UserKnownHostsFile=/dev/null', '-i', 'labsuser.pem', 'labsuser.pem',"ubuntu@" + str(ip) + ":labsuser.pem"])
    time.sleep(180)
    
    print("Proxy instances created successfully ...!")


main()