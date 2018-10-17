#!python3
from pathlib import Path
from operator import itemgetter
import re
import csv
machineNameRE = "OVM_simple_name"
memoryRE = "memory"
cpuRE = "vcpus"
machineList = []
machine = ""
memory= ""
cpu= ""
#Set VirtualMachines directory repository here
pathlist = Path("./VirtualMachines").glob('**/*.cfg')
for path in pathlist:
    path_in_str = str(path)
    id = path_in_str.split("/")[1]
    file = open(path_in_str, "r")
    for line in file:
        if re.search(machineNameRE, line):
            fields = line.strip().split()
            machine = fields[2].replace("'", "")
        if re.search(memoryRE, line):
            fields = line.strip().split()
            memory = int(fields[2]) / 1024
        if re.search(cpuRE, line):
            fields = line.strip().split()
            cpu = fields[2]
    currentMachine = {"name": machine, "memory":memory, "cpu": cpu, "id": id}
    machineList.append(currentMachine)
machineSort = sorted(machineList, key=itemgetter('name')) 
keys = machineSort[0].keys()
with open('machines.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(machineSort)
for x in machineSort:
  print(x)