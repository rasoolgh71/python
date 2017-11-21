import os
import sys
import subprocess
from pprint import pprint

def main():   #print sunprocess
    print("subprocees")
#**********************************************************************************
def subp():   #subprocess list program
    print("subprocess is ")
    out= subprocess.call(['ls'])

    out1=subprocess.Popen(['ls', '-la'])
   # print(subprocess.check_output("df -h".split()).split("\n"))


#**********************************************************************************

def sdisk():  #subprocces list size of disk
    diskinfo = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE)
    output = diskinfo.communicate()[0]
    #for x in output[1:]:
        #if int(x.split()[-2][:-1]) >= 10:
           # print(x)
    print(output)

if __name__=="__main__":
    #main()
    subp()
    sdisk()