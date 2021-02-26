# fetloader.py
# belongs to pasted1337


import configparser
import os
import pkg_resources
import sys

FAIL = '\033[91m'
RESET = "\033[0m"


figlet = """  __     _   _              _                    
 / _|___| |_| |___  __ _ __| |___ _ _  _ __ _  _ 
|  _/ -_)  _| / _ \\/ _` / _` / -_) '_|| '_ \\ || |
|_| \\___|\\__|_\\___/\\__,_\\__,_\\___|_|(_) .__/\\_, |
  b2 - codename bad                    |_|   |__/ 
"""
print(figlet)
print("-- checking for fetloader folder")
hh = os.path.exists("C:\\fetloader.py\\")
ff = os.path.exists("C:\\fetloader.py\\config.ini")
rr = os.path.exists("C:\\fetloader.py\\aye1337nocap.py")
sys.path.append("C:\\fetloader.py\\")
injectorlink = "https://raw.githubusercontent.com/numaru/injector/master/injector.py"

print("-- checking for pywin32")
installed_packages      = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
pkgs = [i.split('==', 1)[0] for i in installed_packages_list]
pywin32installs = pkgs.count("pywin32")

if pywin32installs == 1:
	from win32com.client import GetObject
else:
	os.system("pip install pywin32")
	os.system("pip install pypiwin32")
	from win32com.client import GetObject

print("--- checking for requests")
requestsinstalls = pkgs.count("requests")
if requestsinstalls == 1:
	import requests
else:
	os.system("pip install requests")
	import requests

basecfg = """[fetloader]
cheatrepo = clangremlini/fetloader-dll-repo"""

if hh == False:
	os.system("mkdir C:\\fetloader.py\\")

if ff == False:
	ddd = open("C:\\fetloader.py\\config.ini", "a+")
	ddd.write(basecfg)

if rr == False:
	print("downloading injector library")
	r = requests.get(injectorlink, allow_redirects=True)
	open("C:\\fetloader.py\\aye1337nocap.py", 'wb').write(r.content)
	from aye1337nocap import Injector
	injector = Injector()
else:
	from aye1337nocap import Injector
	injector = Injector()

print("-- initializing config")
config    = configparser.ConfigParser()
config.read("C:\\fetloader.py\\config.ini")
cheatrepo = config['fetloader']['cheatrepo']

try:
	os.remove("C:\\fetloader.py\\cheats.ini")
except(FileNotFoundError):
	pass

cheatrepolink = "https://raw.githubusercontent.com/" + cheatrepo + "/main/cheats.ini"
r = requests.get(cheatrepolink, allow_redirects=True)
open('C:\\fetloader.py\\cheats.ini', 'wb').write(r.content)
print("-- downloaded cheatlist")

config.read("C:\\fetloader.py\\cheats.ini")
cheatsitems = config.items("cheats")

mydict = {}
print("vac - load vac-bypass")

# variables are shitty but idfc
i = 0
for a in cheatsitems:
	d  = list(a)
	c  = list(a)
	i  = i + 1
	aw = str(i)
	mydict['cs' + aw] = d.pop(1)
	print("cs" + aw, sep=' ', end='', flush=True)
	print(" - ", sep=' ', end='', flush=True)
	print(c.pop(0), sep=' ', end='', flush=True)
	print(" - ", sep=' ', end='', flush=True)
	print(mydict['cs' + aw], sep=' ', end='', flush=True)
	print("\n", sep=' ', end='', flush=True)

print("> ", sep=' ', end='', flush=True)
cheatload = input()

if cheatload == "vac":
	r = requests.get("http://github.com/clangremlini/fetloader-dll-repo/raw/main/vac-bypass.exe", allow_redirects=True)
	open("C:\\fetloader.py\\vac-bypass.exe", "wb").write(r.content)
	print("-- downloading vac-bypass.exe")
	os.system("C:\\fetloader.py\\vac-bypass.exe")
	print("-- started vac-bypass.exe")
else:	
	r = requests.get("http://github.com/clangremlini/fetloader-dll-repo/raw/main/emb.exe", allow_redirects=True)
	open("C:\\fetloader.py\\emb.exe", "wb").write(r.content)
	print("-- downloading emb.exe")
	os.system("C:\\fetloader.py\\emb.exe")
	print("-- started emb.exe")
	print("-- getting csgo.exe pid")
	WMI = GetObject('winmgmts:')
	processes = WMI.InstancesOf('Win32_Process')
	process_list = [(p.Properties_("Name").Value, p.Properties_("ProcessID").Value) for p in processes]
	ay = [t for t in process_list if t[0].startswith('csgo.exe')]
	try:
		ad = ay[0]
	except(IndexError):
		print(FAIL + "-- csgo.exe is not started lol" + RESET)
		exit(1)
	ae = list(ad)
	ae.pop(0)
	aq = ae[0]
	ar = str(aq)
	print("-- csgo.exe pid " + ar)
	linkdll = str("https://raw.githubusercontent.com/" + cheatrepo + "/main/" + mydict[cheatload])
	print("-- downloading " + linkdll)
	r = requests.get(linkdll, allow_redirects=True)
	dllpath = str("C:\\fetloader.py\\" + mydict[cheatload])
	open("C:\\fetloader.py\\" + mydict[cheatload], "wb").write(r.content)
	print("-- injecting " + mydict[cheatload])
	injector.load_from_pid(aq)
	injector.inject_dll(dllpath)
	print("injected! now you can close this window")
	time.sleep(5)
