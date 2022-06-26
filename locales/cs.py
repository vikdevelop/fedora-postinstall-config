#!/usr/bin/python3
import os
import sys
#from gettext import gettext as _
HOME = os.path.expanduser('~')
#import checkdistro
print("→ kontrola, jestli se jedná o distribuci Fedora ")
if not os.path.exists("/usr/bin/dnf"):
    print('\033[1m' + 'x-ERROR:' + '\033[0m' + "vypadá to, že na tomto HW není nainstalovaná distribuce Fedora, nebo je poškozená. V takovém případě nemůžete tento skript použít :(")
    exit()
else:
    print('\033[1m' + '→→ OK' + '\033[0m')
print("→→ nyní se vás zeptáme v rámci programu sudo na heslo, protože je potřeba aktualizovat balíčky distribuce Fedora na nejnovější verzi:")
os.system("sudo dnf update -y")
print("→ aktualizace Fedory " + '\033[1m' + 'OK' + '\033[0m')
print('\033[1m' + 'Shrnutí:' + '\033[0m')
print("- kontrola názvu distribuce - OK \n- aktualizace systému - OK \n- konfigurace GRUB + Btrfs a instalace timeshift \n- konfigurace Flathub repositáře a instalace Flatpak aplikací \n- instalace DNF aplikací \n- konfigurace kodeků \n- instalace proprietárního ovladače nVidia")
yn = input("Chcete pokračovat? [Y/n]: ")
if yn == 'n':
    print("Zrušeno.")
    exit()
elif yn == 'y' or 'Y':
    if not os.path.exists("/usr/lib/systemd/system/grub-btrfs.path"):
        # GRUB+BRTFS
        print("→ konfigurace GRUB + Btrfs")
        
        # Timshift & make installation
        print("→→ kontrola jestli je nainstalován timehift a make")
        if not os.path.exists("/usr/bin/timehsift"):
            os.system("sudo dnf install -y timeshift")
        if not os.path.exists("/usr/bin/make"):
            os.system("sudo dnf install -y make")
        
        # Preparing for install grub-btrfs
        print("→→ stahování repozitáře grub-brtfs")
        os.system("cd $HOME/Stažené && git clone https://github.com/Antynea/grub-btrfs")
        os.chdir("%s/Stažené/grub-btrfs" % HOME)
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
        print("→→→ kompilace a instalace pomocí programu make proběhla úspěšně")
        # Activate process grub-btrfs with systemd
        os.system("sudo systemctl enable grub-btrfs.path && sudo systemctl start grub-btrfs.paath")
        # Update GRUB
        os.system("sudo grub2-mkconfig -o /boot/grub2/grub.cfg")
        print("→→ konfigurace GRUB + Btrfs proběhla úspěšně")
    else:
        print("→ GRUB + Btrfs již bylo nakonfigurováno.")
    
    # Enable flatpak repo
    print("→ konfigurace Flathub repositáře")
    os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    # Install Flatpak Apps
    print("→ instalace Flatpak aplikací:")
    flatpakinstall = input("→→ zadejte ID nebo názvy Flatpak aplikací, které chcete nainstalovat (pro přeskočení stiskněte enter): ")
    if flatpakinstall == "":
        print("Přeskakuji.")
    else:
        print("→ instalace Flatpak aplikací:")
        os.system("flatpak install -y %s" % flatpakinstall)
    # installation apps via DNF
    print("→ instalace DNF aplikací:")
    dnfinstall = input("→→ chcete také nainstalovat aplikace přes správce balíčků DNF? [Y/n]: ")
    if dnfinstall == 'n':
        print("Přeskakuji.")
    elif dnfinstall == 'Y' or 'y':
        dnfpkgs = input("→→ zadejte názvy balíčků které chcete nainstalovat: ")
        os.system("sudo dnf install -y %s" % dnfpkgs)
    # Multimedia & codecs
    print("→ Multimédia a kodeky")
    print("→→ Fedora může mít občas problémy s kodeky. Pokud chcete, můžete si nainstalovat přehrávač VLC media player jako Flatpak a problémům s kodeky se vyhnete.")
    vlcflatpak = input("Chcete tedy nainstalovat program VLC media player jako Flatpak? [Y/n]: ")
    if vlcflatpak == 'n':
        print("Přeskakuji.")
    elif vlcflatpak == 'Y' or 'y':
        if not os.path.exists("/var/lib/flatpak/app/org.videolan.VLC"):
            os.system("flatpak install -y org.videolan.VLC")
        else:
            print("→→ VLC již bylo nainstalováno.")
    
    # NVIDIA proprietary graphic card driver installation
    nvidia = input("Přejete si nainstalovat proprietární ovladač nVidia (v případě že máte GPU od společnosti nVidia)? [Y/n]: ")
    if nvidia == 'n':
        print("Přeskakuji.")
    elif nvidia == 'y' or 'Y':
        print("→ instalování prop. ovladače nVidia Linux akmod graphic card driver:")
        os.system("sudo dnf install -y akmod-nvidia")
        print('\033[1m' + '→→ OK' + '\033[0m')
    print('\033[1m' + '→ post-konfigurace Fedory proběhla úspěšně!' + '\033[0m')
