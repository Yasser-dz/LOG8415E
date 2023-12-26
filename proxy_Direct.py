import pymysql
import sys
import math
import random
from pythonping import ping
from sshtunnel import SSHTunnelForwarder


master_public_ip = "172.31.17.2"
slaves_public_ip = ["172.31.17.3", "172.31.17.4", "172.31.17.5"]


def execute(slave_ip, master_ip, query):
    """
    execute uses the SSHTunnelForwarder class from the sshtunnel library to create an SSH tunnel
    between the slave and master servers. This allows the function to execute the MySQL query on 
    the master server as if it were running on the slave server.
    : param slave_ip:    A string that represents the IP address of the slave node
    : param master_ip:   A string that represents the IP address of the master node
    : query:             A string that represents a MySQL query that will be executed on the given server
    : return:             The pymsql connection
    """
    with SSHTunnelForwarder(slave_ip, ssh_username='ubuntu', ssh_pkey='labsuser.pem', remote_bind_address=(master_ip, 3306)) as tunnel:
        conn = pymysql.connect(host=master_ip, user='root', password='root', db='sakila', port=3306, autocommit=True)
        cursor = conn.cursor()
        operation = query
        cursor.execute(operation)
        print(cursor.fetchall())
        return conn

def direct_hit(master, query):
    """
    direct_hit calls the execute method on the master server
    : param master:     A string that represents the IP address of the master server
    : param query:      The SQL query to execute on the MySQL server          
    """
    print('Request sent to Master -', master, '\n')
    execute(master, master, query)


def main():
    if len(sys.argv) < 2:
        print('ERROR! Make sure the command has the query, like this => python3 proxy.py "SQL QUERY"')
    else:
        query = sys.argv[1]
        direct_hit(master_public_ip, query)
        
    print("=====================================================================================================================")

        
main()