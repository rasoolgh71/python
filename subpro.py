import os
import sys
import subprocess

def main():
    print("subprocees")
def subp():
    print("subprocess is ")
    out= subprocess.call('ls')
    print('out is:',out)
    out1=subprocess.Popen(['ls','-la'])
    print('ou is:',out1)


if __name__=="__main__":
    #main()
    subp()