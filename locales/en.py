#!/usr/bin/python3
import os
import sys
#from gettext import gettext as _
HOME = os.path.expanduser('~')
#import checkdistro
print("→ checking if it is a Fedora distribution ")
if not os.path.exists("/usr/bin/dnf"):
    print('\033[1m' + 'x-ERROR:' + '\033[0m' + "it looks like the Fedora distribution is not installed on this HW, or it is corrupted. In this case, you cannot use this script :(")
    exit()
else:
    print('\033[1m' + '→→ OK' + '\033[0m')
print("→→ we will now ask you for your password within sudo because we need to update the Fedora distribution packages to the latest version:")
os.system("sudo dnf update -y")
print("→ updatation Fedora " + '\033[1m' + 'OK' + '\033[0m')
print('\033[1m' + 'Summary:' + '\033[0m')
print("- checking name of distro - OK \n- updatation of system - OK \n- configuration GRUB + Btrfs a installation timeshift \n- configuration Flathub repository a installation Flatpak apps \n- installation DNF apps \n- configuration codecs \n- instlallation proprietary driver nVidia")
yn = input("Would you like to continue? [Y/n]: ")
if yn == 'n':
    print("Canceled.")
    exit()
if yn == 'y' or 'Y':
    if not os.path.exists("/usr/lib/systemd/system/grub-btrfs.path"):
        # GRUB+BRTFS
        print("→ configuration GRUB + Btrfs")
        
        # Timshift & make installation
        print("→→ checking if is installed timehift and make")
        if not os.path.exists("/usr/bin/timehsift"):
            os.system("sudo dnf install -y timeshift")
        if not os.path.exists("/usr/bin/make"):
            os.system("sudo dnf install -y make")
        
        # Preparing for install grub-btrfs
        print("→→ downloading repository grub-brtfs")
        os.system("cd $HOME/Downloads && git clone https://github.com/Antynea/grub-btrfs")
        os.chdir("%s/Downloads/grub-btrfs" % HOME)
        # config file of grub-btrfs
        with open("config", "w") as c:
            c.write('GRUB_BTRFS_GRUB_DIRNAME="/boot/grub2"\n')
            c.write('GRUB_BTRFS_BOOT_DIRNAME="/boot"\n')
            c.write('GRUB_BTRFS_SCRIPT_CHECK=grub2-script-check')
        
        # grub-btrfs.path file
        with open("grub-btrfs.path", "w") as p:
            p.write('[Unit]\n')
            p.write('Description=Monitors for new snapshots\n')
            p.write('DefaultDependencies=no\n')
            p.write('Requires=run-timeshift-backup.mount\n')
            p.write('After=run-timeshift-backup.mount\n')
            p.write('BindsTo=run-timeshift-backup.mount\n')
            p.write('\n')
            p.write('[Path]\n')
            p.write('PathModified=/run/timeshift/backup/timeshift-btrfs/snapshots\n')
            p.write('\n')
            p.write('[Install]\n')
            p.write('WantedBy=run-timeshift-backup.mount')
        
        # Installation grub-btrfs
        os.system("sudo make install")
        print("→→→ compilation & installation with program make was successfull")
        # Activate process grub-btrfs with systemd
        os.system("sudo systemctl enable grub-btrfs.path && sudo systemctl start grub-btrfs.paath")
        # Update GRUB
        os.system("sudo grub2-mkconfig -o /boot/grub2/grub.cfg")
        print("→→ configuration GRUB + Btrfs was successfull")
    else:
        print("→ GRUB + Btrfs already configured.")
    
    # Enable flatpak repo
    print("→ configuration Flatpak-Flathub repo")
    os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    # Install Flatpak Apps
    print("→ installation of Flatpak apps:")
    flatpakinstall = input("→→ enter IDs or names of Flatpak apps want you install (for skip press enter): ")
    if flatpakinstall == "":
        print("I skiping.")
    else:
        os.system("flatpak install -y %s" % flatpakinstall)
    # installation apps via DNF
    print("→ installation DNF apps:")
    dnfinstall = input("→→ want you install too apps via DNF package manager? [Y/n]: ")
    if dnfinstall == 'n':
        print("I skiping.")
    elif dnfinstall == 'Y' or 'y':
        dnfpkgs = input("→→ enter name of packages want you install: ")
        os.system("sudo dnf install -y %s" % dnfpkgs)
    # Multimedia & codecs
    print("→ Multimedia a codecs")
    print("→→ Fedora may occasionally have problems with codecs. If you want, you can install VLC media player as Flatpak and you can avoid codec problems.")
    vlcflatpak = input("So you want to install VLC media player as Flatpak? [Y/n]: ")
    if vlcflatpak == 'n':
        print("I skiping.")
    elif vlcflatpak == 'Y' or 'y':
        if not os.path.exists("/var/lib/flatpak/app/org.videolan.VLC"):
            os.system("flatpak install -y org.videolan.VLC")
        else:
            print("→→ VLC was installed.")
    # NVIDIA proprietary graphic card driver installation
    nvidia = input("Do you wish to install a proprietary nVidia driver (in case you have an nVidia GPU)? [Y/n]: ")
    if nvidia == 'n':
        print("I skiping.")
    elif nvidia == 'y' or 'Y':
        print("→ installation proprietary driver nVidia Linux akmod graphic card driver:")
        os.system("sudo dnf install -y akmod-nvidia")
        print('\033[1m' + '→→ OK' + '\033[0m')
    print('\033[1m' + '→ post-configuration of Fedora was successfull!' + '\033[0m')
