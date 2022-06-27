#!/usr/bin/python3
import os
if os.path.exists("/dev/nvidia0"):
    print("-")
else:
    print("→ installation of program CoreCtrl for simple settings GPUs by AMD")
    corectrl = input("→→ so do you wish install corectrl? [Y/n]: ")
    if corectrl == 'n':
        print("I skiping.")
    elif corectrl == 'Y' or 'y':
        os.system("sudo dnf install -y corectrl")
