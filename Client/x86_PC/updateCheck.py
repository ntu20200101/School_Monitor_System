import os
import datetime
import subprocess
import time

updateCheck = 0
preDate = 0

while (True):
    print(str(datetime.datetime.now()), "check wating time ...")
    timeInfo = datetime.datetime.strftime(datetime.datetime.now(), "%d-%H")
    if (preDate != int(timeInfo.split("-")[0])):
        preDate = int(timeInfo.split("-")[0])
        updateCheck = 0
    if (int(timeInfo.split("-")[1]) == 6 and updateCheck == 0):
        print(str(datetime.datetime.now()), "checking github online code ...")
        updateCheck = 1
        os.chdir("/home/ubuntu/School_Monitor_System/")
        updateInfo = subprocess.Popen(["sudo", "git", "pull"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        updateStatus, stderr = updateInfo.communicate()
        if not (updateStatus.decode("utf-8") == "Already up to date.\n"):
            print(str(datetime.datetime.now()), "updating online code ...")
            os.system("python3 /home/ubuntu/School_Monitor_System/Client/x86_PC/environment.py")
        else:
            print(str(datetime.datetime.now()), "nothing update ...")
    time.sleep(300)
    