import os,time,platform
os.system('clear')
import os, platform, time, sys
class TUTUL:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.070)
TUTUL('\033[97;1m[\033[92;1m+\033[97;1m]\033[20;92m CHECKING UPDATES-!✅')
time.sleep(2)
os.system('xdg-open https://www.facebook.com/Tutul.King.Ok.Bro')
#os.system('pip install requests mechanize bs4 rich')#
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import DM64
elif bit=='32bit':
    import DM32
