import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from PUB64 import Menu
 
        Menu()
 
 
 
elif bit == "32bit":
 
        from Coming import Manu
 
 
        Main()
 
 
 
