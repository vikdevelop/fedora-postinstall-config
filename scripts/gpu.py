#!/usr/bin/python3
import os
import sys
sys.path.append("/tmp/fedora-postinstall-config/locales")
from en import *
if os.path.exists("/dev/nvidia0"):
    print(nvidiagpu_installation_title)
    nvidia = input(nvidiagpu_installation_input)
    if nvidia == 'n':
        print(nvidiagpu_skip)
    elif nvidia == 'y' or 'Y':
        print(update_before_installation_nvidiagpu)
        os.system("sudo dnf update --refresh -y > /dev/null 2>&1")
        print("Installing NVIDIA proprietary driver.\n - it's gonna take a while")
        os.system("sudo dnf install -y akmod-nvidia > /dev/null 2>&1")
        print('\033[1m' + '→→ OK' + '\033[0m')
        print('\033[93m' + nvidiagpu_warning_restart)
else:
    print(corectrl_title)
    corectrl = input(corectrl_input)
    if corectrl == 'n':
        print(corectrl_skip)
    elif corectrl == 'Y' or 'y':
        print("Installing CoreCtrl ...")
        os.system("sudo dnf install -y corectrl > /dev/null 2>&1")
        print('\033[92m' + corectrl_status)
#print('\033[1m' + 'post-configuration of Fedora was successfull!' + '\033[0m')
