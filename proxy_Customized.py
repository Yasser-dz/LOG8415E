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


def ping_host(host):
    """
    ping_host uses the ping function from the sh library to send a single ICMP echo request 
    to the specified host and returns the average round-trip time (RTT) in milliseconds.
    : param host:    A string that represents the hostname or IP address of the host that is being pinged.
    : return:        The average round-trip time in milliseconds
    """
    return ping(target=host, count=1, timeout=2).rtt_avg_ms


def get_fastest_slave(slaves):
    """
    get_fastest_slave uses a loop to iterate over the list of slaves and measures the ping time 
    to each slave using the ping_host function. It then stores the slave with the lowest ping time 
    in a variable called fastest_slave and returns it at the end of the function.
    : param slaves:     List of slave instances
    : return:           Fastest slave from the list of slave nodes            
    """
    min = math.inf
    fastest_slave = None

    for slave in slaves:
        ping_time = ping_host(slave)
        print("Slave", slaves_public_ip.index(slave) + 1, "ping time:", ping_time)
        
        if ping_time < min:
            fastest_slave = slave
            min = ping_time
    
    print('Lowest Ping : Slave', slaves_public_ip.index(fastest_slave) + 1, "with", min, '\n')
    return fastest_slave



def customized_hit(slaves, master, query):
    """
    customized_hit calls the execute method on the fastest slave server
    : param slaves:     List of slave instances
    : param master:     A string that represents the IP address of the master server
    : param query:      The SQL query to execute on the MySQL server          
    """
    fastest_slave = get_fastest_slave(slaves)
    print('Request sent to Slave', slaves_public_ip.index(fastest_slave) + 1, '-', fastest_slave, '\n')
    execute(fastest_slave, master, query)


def main():
    if len(sys.argv) < 2:
        print('ERROR! Make sure the command has the query, like this => python3 proxy.py "SQL QUERY"')
    else:
        query = sys.argv[1]
        customized_hit(slaves_public_ip, master_public_ip, query)
        
    print("=====================================================================================================================")

        
main()