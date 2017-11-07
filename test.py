import sys
import os
import subprocess
import socket
import fcntl
import struct
import array
import psutil
import re
from collections import namedtuple
DiskUsage = namedtuple('DiskUsage', 'total used free')

def sort():
    list1 = [1, 9, 80000, 2, 7, 4, 6]
    for item in list1:
        item = int(item)
        list1.sort()
    print(list1)
#********************************************************************
def diskio():
    print("virtual memory :", psutil.virtual_memory()) #virtual memory
    print("cpu :", psutil.cpu_times()) #cpu
    #disk=psutil.disk_usage('/')
    print("disk i/o:", psutil.disk_io_counters(perdisk=False))#read write disk

#*************************************************************************
def get_interface(external=False ,ip=False):
    name_pattern = "^(\w+)\s"
    mac_pattern = ".*?HWaddr[ ]([0-9A-Fa-f:]{17})" if external else ""
    ip_pattern = ".*?\n\s+inet[ ]addr:((?:\d+\.){3}\d+)" if ip else ""
    pattern = re.compile("".join((name_pattern, mac_pattern, ip_pattern)),
                         flags=re.MULTILINE)
    ifconfig = subprocess.check_output("ifconfig").decode()
    interfaces = pattern.findall(ifconfig)
    if external or ip:
        Interface = namedtuple("Interface", "name {mac} {ip}".format(
            mac="mac" if external else "",
            ip="ip" if ip else ""))
        return [Interface(*interface) for interface in interfaces]
    else:
        return interfaces
#*********************************************************************
def network():
    name = socket.gethostbyname(socket.gethostname())
    print("ip address is:",name)
    print(psutil.net_io_counters(pernic=True))
    #psutil.test()
#**********************************************************
def send():
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 50007  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()
#********************************************************************************
def recive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))

    # Receive no more than 1024 bytes
    tm = s.recv(1024)

    s.close()

    print("The time got from the server is %s" % tm.decode('ascii'))


#******************************************************************************8
def disk_usage():
    st = os.statvfs('/home')
    free = (st.f_frsize * st.f_bavail)/1000000000    #free
    total =( st.f_frsize * st.f_blocks)/1000000000    #total
    use =((st.f_blocks - st.f_bavail) * st.f_frsize)/1000000000
    percent = (float(use) / total) * 100
    print("free space is:",free,"G")
    print("total space is:",total,"G")
    print("use space is:",use,"G")
    print("percentage is:",percent,"%")
    f = os.popen("df -h")
    for i in f.readlines():
        print("myresult : ", i)
#***********************************************************************


if __name__ == "__main__":
    network()
    disk_usage()
    interfaces = get_interface(external=True, ip=True)
    for interface in interfaces:
        print("{name}: {ip}".format(name=interface.name, ip=interface.ip))
    diskio()




