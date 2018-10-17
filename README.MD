# Python script to get OVM config on Exalogic environments

## Set VirtualMachines Path

Set the variable pathlist according to OVM Repo to find all .cfg files used by vServers.

## Python version

This script was test in python v3. 

## Run

Copy get-machine-conf.py script to any computer node (cn01 for ex) and execute:

```sh
python3 get-machine-conf.py
```

## Export CSV

This script also exports the result to csv file called **machines.csv** created at the same py script directory.