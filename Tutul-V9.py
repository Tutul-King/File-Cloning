import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from COOKIES64 import main
 
        main()
 
 
 
elif bit == "32bit":
 
        from COOKIE32 import main
 
 
        main()
 
