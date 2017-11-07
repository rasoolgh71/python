import sys
import os
import subprocess
from collections import namedtuple
DiskUsage = namedtuple('DiskUsage', 'total used free')
def sort():
    list1=[1, 9, 80000, 2, 7, 4, 6]
    for item in list1:
        item=int(item)
        list1.sort()
    print(list1)
print("hi rasool")
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


if __name__=="__main__":
    #sort()
    disk_usage()




