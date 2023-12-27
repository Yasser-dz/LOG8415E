import pymysql
import random
import sys
import math
from pythonping import ping
from sshtunnel import SSHTunnelForwarder
from flask import Flask, request, jsonify


master_public_ip = "172.31.17.3"
slaves_public_ip = ["172.31.17.4", "172.31.17.5", "172.31.17.6"]

app = Flask(__name__)


@app.route('/endpoint', methods=['GET', 'POST'])
def handle_gatekeeper_request():
    # Extract the strategy from the parameters
    strategy = request.args.get('strategy')

    # Extract the query from the request data
    query = request.get_data(as_text=True)

    if strategy == "direct":
        ip = direct_hit()
    elif strategy == "random":
        ip = random_hit()
    elif strategy == "customized":
        ip = customized_hit()
    else:
        raise ValueError("Invalid strategy")

    # Forward the request to the chosen ip of node
    result = execute(ip, query)
    return jsonify(result)


def execute(slave_ip, query):
   
    with SSHTunnelForwarder(slave_ip, ssh_username='ubuntu', ssh_pkey='labsuser.pem', remote_bind_address=(master_public_ip, 3306)) as tunnel:
        conn = pymysql.connect(host=master_public_ip, user='root', password='root', db='sakila', port=3306, autocommit=True)
        cursor = conn.cursor()
        operation = query
        cursor.execute(operation)
        result =cursor.fetchall()
        print(result)
        conn.close
        return result

def direct_hit(): 
    print('Request sent to Master -', master_public_ip, '\n')
    return master_public_ip



def get_random_slave(slaves_public_ip):
    return random.choice(slaves_public_ip)



def random_hit():
    slave = get_random_slave(slaves_public_ip)
    print('Request sent to Slave', slaves_public_ip.index(slave) + 1, '-', slave, '\n')
    return slave


def ping_host(host):
    return ping(target=host, count=1, timeout=2).rtt_avg_ms


def get_fastest_slave(slaves_public_ip):
    min = math.inf
    fastest_slave = None
    for slave in slaves_public_ip:
        ping_time = ping_host(slave)
        print("Slave", slaves_public_ip.index(slave) + 1, "ping time:", ping_time)
        
        if ping_time < min:
            fastest_slave = slave
            min = ping_time
    
    print('Lowest Ping : Slave', slaves_public_ip.index(fastest_slave) + 1, "with", min, '\n')
    return fastest_slave

def customized_hit():
    fastest_slave = get_fastest_slave(slaves_public_ip)
    print('Request sent to Slave', slaves_public_ip.index(fastest_slave) + 1, '-', fastest_slave, '\n')
    return fastest_slave
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)