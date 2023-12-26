#!/bin/bash

# Prepare the NDB Cluster database for sysbench OLTP read-write test
sudo sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root --mysql-password=ClusterPassword --mysql_storage_engine=ndbcluster prepare

# Run sysbench OLTP read-write test on the NDB Cluster with specific configurations and redirect output to clusterResult.txt
sudo sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root --mysql-password=ClusterPassword --mysql_storage_engine=ndbcluster --num-threads=6 --max-time=60 --max-requests=0 run > clusterResult.txt

# Cleanup the NDB Cluster database after sysbench OLTP read-write test
sudo sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root --mysql-password=ClusterPassword --mysql_storage_engine=ndbcluster cleanup
