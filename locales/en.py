#!/usr/bin/python3
import os
import sys
HOME = os.path.expanduser('~')
print("→ checking if it is a Fedora distribution ")
if not os.path.exists("/usr/bin/dnf"):
    print('\033[1m' + 'x-ERROR:' + '\033[0m' + "it looks like the Fedora distribution is not installed on this HW, or it is corrupted. In this case, you cannot use this script :(")
    exit()
else:
    print('\033[1m' + '→→ OK' + '\033[0m')
print("→→ we will now ask you for your password within sudo that choosed in installation of Fedora, because we need to update the Fedora distribution packages to the latest version:")
os.system("sudo dnf update -y")
print("→ updatation Fedora " + '\033[1m' + 'OK' + '\033[0m')
print('\033[1m' + 'Summary:' + '\033[0m')
print("- checking name of distro - OK \n- updatation of system - OK \n- configuration GRUB + Btrfs a installation timeshift \n- configuration Flathub repository a installation recommended Flatpak apps \n- configuration codecs \n- instlallation proprietary driver nVidia")
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
print("→ installation recommended Flatpak apps")
    skip = input("If you want, you can skip this step by pressing the enter key (press the c key to continue): ")
    if skip == "":
        print("I skiping.")
    elif skip == "c":
        flatseal = input("Do you want install the Flatseal app that allows you to set permissions on Flatpak apps? [Y/n]: ")
        em = input("Do you want to install the Extension Manager application that allows you to manage extensions for GNOME (Fedora Workstation edition)? [Y/n]: ")
        dw = input("Do you want to install Dynamic Wallpaper, an application that allows you to set transient wallpapers in GNOME? [Y/n]: ")
        if flatseal == 'n':
            print("...")
        elif flatseal == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.github.tchx84.Flatseal"):
                os.system("flatpak install -y com.github.tchx84.Flatseal")
            else:
                print("Flatseal already installed.")
        if em == 'n':
            print("...")
        elif em == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.mattjakeman.ExtensionManager"):
                os.system("flatpak install -y com.mattjakeman.ExtensionManager")
            else:
                print("Extension Manager already installed.")
        if dw == 'n':
            print("...")
        elif dw == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/me.dusansimic.DynamicWallapaper"):
                os.system("flatpak install -y me.dusansimic.DynamicWallapaper")
            else:
                print("Dynamic Wallpaper already installed.")
    print("→ multimedia codecs")
    print("→→ sometimes you may encounter potential problems with codecs in the web browser (but also in other applications).")
    codecs = input("→→→ do you wish to install additional multimedia codecs? [Y/n]: ")
    print("→ installation nVidia proprietary driver")
    nvidia = input("→→ do you wish to install a proprietary nVidia driver (in case you have an nVidia GPU)?? [Y/n]: ")
    if codecs == 'n':
        print("I skiping.")
    elif codecs == 'Y' or 'y':
        os.system("sudo dnf groupupdate -y multimedia --setop='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin > /dev/null 2>&1 && sudo dnf groupupdate -y sound-and-video > /dev/null 2>&1")
    # NVIDIA proprietary graphic card driver installation
    if nvidia == 'n':
        print("I skiping.")
    elif nvidia == 'y' or 'Y':
        print("→ before installing a proprietary nvidia driver, first check for other updates:")
        os.system("sudo dnf update --refresh -y")
        print("→ installing proprietary driver nVidia Linux akmod graphic card driver:")
        os.system("sudo dnf install -y akmod-nvidia")
        print('\033[1m' + '→→ OK' + '\033[0m')
    print('\033[1m' + '→ post installation configuration of Fedora was successfull"' + '\033[0m')
