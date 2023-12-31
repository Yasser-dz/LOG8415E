#!/bin/bash

# Prepare the database for sysbench OLTP read-write test
sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root prepare

# Run sysbench OLTP read-write test with specific configurations and redirect output to standaloneResult.txt
sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root --num-threads=6 --max-time=60 --max-requests=0 run > standaloneResult.txt

# Cleanup the database after sysbench OLTP read-write test
sysbench oltp_read_write --table-size=100000 --mysql-db=sakila --db-driver=mysql --mysql-user=root cleanup
