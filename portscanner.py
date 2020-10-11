#!/usr/ rkt python
import os
import sys
import socket
os.system("clear")

# color & banner code
from colorama import init
init()
from termcolor import cprint
from pyfiglet import figlet_format
cprint (figlet_format('Port Scanner'),'blue',attrs=['bold']) 



print (chr(27)+"[35m"+"                                                      version : 2.0")
print (chr(27)+"[34m"+"           Author : Rahat Khan Tusar(RKT)")
print (chr(27)+"[34m"+"           Github : https://github.com/r3k4t")
print



print (chr(27)+"[36m")
ip = input("Enter the host to be scanned(Ex:amazon.com,google.com etc): ")
rkt_port_list = [80,443,1900,53,20,21,22,23,8080,25000]


# For loop
for port in rkt_port_list:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    r = sock.connect_ex((ip,port))


# if & else loop
    if r == 0 :
        print (chr(27)+"[32m")
        print ('Port',port,'open')
    else:
        print (chr(27)+"[31m")
        print ('Port',port,'closed') 
