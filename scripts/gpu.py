#!/usr/bin/python3
import os
import sys
import subprocess
sys.path.append("/tmp/fedora-postinstall-config/locales")
from en import *
if subprocess.getoutput('glxinfo | grep "Vendor"') == "    Vendor: nouveau (0x10de)":
    print('\033[1m' + nvidiagpu_installation_title + '\033[0m')
    nvidia = input(nvidiagpu_installation_input)
    if nvidia == 'n':
        print(nvidiagpu_skip)
    elif nvidia == 'y' or 'Y':
        print(update_before_installation_nvidiagpu)
        os.system("sudo dnf update --refresh -y > /dev/null 2>&1")
        print("Installing NVIDIA proprietary driver.\n - it's gonna take a while")
        os.system("sudo dnf install -y akmod-nvidia > /dev/null 2>&1")
        print('\033[1m' + '→→ OK' + '\033[0m')
        print('\033[93m' + nvidiagpu_warning_restart + '\033[0m')
else:
    print('\033[1m' + corectrl_title + '\033[0m')
    corectrl = input(corectrl_input)
    if corectrl == 'n':
        print(corectrl_skip)
    elif corectrl == 'Y' or 'y':
        print("Installing CoreCtrl ...")
        os.system("sudo dnf install -y corectrl > /dev/null 2>&1")
        print('\033[92m' + corectrl_status + '\033[0m')
