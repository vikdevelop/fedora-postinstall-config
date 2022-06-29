#!/usr/bin/python3
import os
if os.path.exists("/dev/nvidia0"):
    print("→ installation of proprietary driver by nVidia")
    nvidia = input("→→ do you wish install proprietary driver by nVidia? [Y/n]: ")
    # NVIDIA proprietary graphic card driver installation
    if nvidia == 'n':
        print("I skiping.")
    elif nvidia == 'y' or 'Y':
        print("→ before installation proprietary driver, we first check, if updates avaible again:")
        os.system("sudo dnf update --refresh -y")
        print("→ installing proprietary nVidia Linux akmod graphic card driver:")
        os.system("sudo dnf install -y akmod-nvidia")
        print('\033[1m' + '→→ OK' + '\033[0m')
        print('\033[93m' + 'For your nVidia GPU settings to take effect, you need to restart your computer' + '\033[93m')
else:
    print("→ installation of program CoreCtrl for simple settings GPUs by AMD")
    corectrl = input("→→ so do you wish install corectrl? [Y/n]: ")
    if corectrl == 'n':
        print("I skiping.")
    elif corectrl == 'Y' or 'y':
        os.system("sudo dnf install -y corectrl")
