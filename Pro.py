import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
xoss('\033[0;92m\033[1;37m[\u001b[36m+\033[1;37m] \033[0;92mWaiting For Update...? ')
time.sleep(5)
xoss('\033[0;92m\033[1;37m[\u001b[36m•\033[1;37m]\033[0;93m My Facebook Account')
time.sleep(3)
os.system('xdg-open https://www.facebook.com/Tutul.King.Ok.Bro')