import subprocess
import csv
import os

cmd = ["ping"]

hardwarefile = os.path.join(os.path.dirname(__file__), 'list.csv')

with open(hardwarefile, newline='') as csvfile:
    hardwarelist = csv.reader(csvfile)
    for row in hardwarelist:
        cmd.append(row[1])
        r = subprocess.call(cmd, stdout=subprocess.PIPE)
        cmd.pop()
        if r:
            print('\033[0;31mNOK\033[0m : [\033[0;31m' + row[1] + '\033[0m]\t \033[0;31m' + row[0] + '\033[0m')
        else:
            print('\033[0;32mOK\033[0m : [' + row[1] + ']\t ' + row[0])
