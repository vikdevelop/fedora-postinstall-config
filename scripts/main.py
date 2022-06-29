#!/usr/bin/python3
import os
import sys
import subprocess
import json
#HOME = os.path.expanduser('~')
sys.path.append("/tmp/fedora-postinstall-config/")
from fedora_postinstall_config import *
print(checking)

if not os.path.exists("/usr/bin/dnf"):
    print('\033[1m' + 'x-ERROR:' + '\033[0m' + xerror)
    exit()
else:
    print('\033[1m' + '→→ OK' + '\033[0m')
print(sudo)
print(update_will_take_time)
os.system("sudo dnf update -y > /dev/null 2>&1")
print(update_status + '\033[1m' + 'OK' + '\033[0m')
print('\033[1m' + summary_title + '\033[0m')
print(summary_description)
yn = input(continueyn + " [Y/n]: ")
if yn == 'n':
    print(canceled)
    exit()
elif yn == 'y' or 'Y':
    if not os.path.exists("/usr/lib/systemd/system/grub-btrfs.path"):
        # GRUB+BRTFS
        print(grub_btrfs_title)
        
        # Timshift & make installation
        print(timeshift_make)
        if not os.path.exists("/usr/bin/timehsift"):
            print(installing_timeshift)
            os.system("dnf install -y timeshift > /dev/null 2>&1")
        if not os.path.exists("/usr/bin/make"):
            print(installing_make)
            os.system("dnf install -y make > /dev/null 2>&1")
        
        # Preparing for install grub-btrfs
        print(grub_btrfs_downloading)
        os.system("git clone https://github.com/Antynea/grub-btrfs /tmp/fedora-postinstall-config/grub-btrfs > /dev/null 2>&1")
        os.chdir("/tmp/fedora-postinstall-config/grub-btrfs")
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
        print(make_status)
        # Activate process grub-btrfs with systemd
        os.system("sudo systemctl enable grub-btrfs.path > /dev/null 2>&1 && sudo systemctl start grub-btrfs.paath > /dev/null 2>&1")
        # Update GRUB
        os.system("sudo grub2-mkconfig -o /boot/grub2/grub.cfg > /dev/null 2>&1")
        print(grub_btrfs_status)
    else:
        print(grub_btrfs_already_configured)
    
    # Enable flatpak repo
    print(flathub_repo_status)
    os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    # Multimedia & codecs
    print(flatpak_installation_title)
    skip = input(flatpak_installation_desc)
    if skip == "":
        print(skip_flatpakinstall)
    elif skip == "c":
        flatseal = input(flatseal)
        em = input(em)
        dw = input(dw)
        if flatseal == 'n':
            print("...")
        elif flatseal == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.github.tchx84.Flatseal"):
                os.system("flatpak install -y com.github.tchx84.Flatseal > /dev/null 2>&1")
            else:
                print(flatseal_installed_status)
        if em == 'n':
            print("...")
        elif em == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.mattjakeman.ExtensionManager"):
                os.system("flatpak install -y com.mattjakeman.ExtensionManager > /dev/null 2>&1")
            else:
                print(em_installed_status)
        if dw == 'n':
            print("...")
        elif dw == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/me.dusansimic.DynamicWallpaper > /dev/null 2>&1"):
                os.system("flatpak install -y me.dusansimic.DynamicWallpaper")
            else:
                print(dw_installed_status)
    print(media_codecs_title)
    print(media_codecs_desc)
    codecs = input(codecs_input)
    print(dnf_speedup_title_desc)
    dnf = input(dnf_input)
    # Import gpu script
    #sys.path.append("/tmp/fedora-postinstall-config/scripts")
    #import gpu
    #os.system("python3 /tmp/fedora-postinstall-config/scripts/gpu.py")
    if dnf == 'n':
        print(skip_dnf_speedup)
    elif dnf == 'Y' or 'y':
        os.system("pkexec python3 /tmp/fedora-postinstall-config/scripts/dnf-fast.py")
        print(dnf_speedup_successfull)
    if codecs == 'n':
        print(skip_codecs_installation)
    elif codecs == 'Y' or 'y':
        os.system("sudo dnf groupupdate -y multimedia --setop='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin > /dev/null 2>&1 && sudo dnf groupupdate -y sound-and-video > /dev/null 2>&1")
    print('\033[1m' + postinstall_config_successfull + '\033[0m')
