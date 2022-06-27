#!/usr/bin/python3
import os
import sys
import subprocess
HOME = os.path.expanduser('~')
print("→ kontrola, jestli se jedná o distribuci Fedora ")
if not os.path.exists("/usr/bin/dnf"):
    print('\033[1m' + 'x-ERROR:' + '\033[0m' + "vypadá to, že na tomto HW není nainstalovaná distribuce Fedora, nebo je poškozená. V takovém případě nemůžete tento skript použít :(")
    exit()
else:
    print('\033[1m' + '→→ OK' + '\033[0m')
print("→→ nyní se vám zobrazí výzva pro zadání hesla, které jste zvolili při instalaci Fedory, protože je potřeba aktualizovat balíčky distribuce Fedora na nejnovější verzi:")
os.system("sudo dnf update -y")
print("→ aktualizace Fedory " + '\033[1m' + 'OK' + '\033[0m')
print('\033[1m' + 'Shrnutí:' + '\033[0m')
print("- kontrola názvu distribuce - OK \n- aktualizace systému - OK \n- konfigurace GRUB + Btrfs a instalace timeshift \n- konfigurace Flathub repositáře a instalace Flatpak aplikací \n- konfigurace kodeků \n- zrychlení DNF \n- instalace volitelného SW pro vaší grafickou kartu")
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
            os.system("dnf install -y timeshift")
        if not os.path.exists("/usr/bin/make"):
            os.system("dnf install -y make")
        
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
    print("→ přidávání Flathub repositáře")
    os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    # Multimedia & codecs
    print("→ instalace doporučených Flatpak aplikací")
    skip = input("Jestli chcete, můžete tento krok přeskočit stisknutím klávesy enter (pro pokračování stiskněte klávesu c): ")
    if skip == "":
        print("instalace Flatpak aplikací: přeskakuji.")
    elif skip == "c":
        flatseal = input("Chcete nainstalovat aplikaci Flatseal, která umožňuje nastavovat oprávnění aplikací Flatpak? [Y/n]: ")
        em = input("Chcete nainstalovat aplikaci Extension Manager, která umožňuje spravovat rozšíření pro prostředí GNOME (edice Fedora Workstation)? [Y/n]: ")
        dw = input("Chcete nainstalovat aplikaci Dynamic Wallpaper (Dynamická tapeta), která umožňuje nastavování přechodných tapet v prostředí GNOME? [Y/n]: ")
        if flatseal == 'n':
            print("...")
        elif flatseal == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.github.tchx84.Flatseal"):
                os.system("flatpak install -y com.github.tchx84.Flatseal")
            else:
                print("Flatseal je již nainstalovaný.")
        if em == 'n':
            print("...")
        elif em == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/com.mattjakeman.ExtensionManager"):
                os.system("flatpak install -y com.mattjakeman.ExtensionManager")
            else:
                print("Extension Manager je již nainstalovaný.")
        if dw == 'n':
            print("...")
        elif dw == 'Y' or 'y':
            if not os.path.exists("/var/lib/flatpak/app/me.dusansimic.DynamicWallapaper"):
                os.system("flatpak install -y me.dusansimic.DynamicWallapaper")
            else:
                print("Dynamic Wallpaper je již nainstalovaný.")
    print("→ multimediální kodeky")
    print("→→ občas se můžete setkat s potenciálními problémy s kodeky ve webovém prohlížeči (ale i u jiných aplikací).")
    codecs = input("→→→ přejete si tedy nainstalovat dodatečné multimediální kodeky? [Y/n]: ")
    print("→ zrychlení správce balíčků DNF\n→→ DNF patří k těm pomalejším správcům balíčků. Je však možné ho zrychlit.")
    dnf = input("→→→ přejete si tedy zrychlit správce balíčků dnf? [Y/n]: ")
    os.system("python3 /tmp/fedora-postinstall-config/scripts/gpu.py")
    if dnf == 'n':
        print("zrychlení dnf: přeskakuji.")
    elif dnf == 'Y' or 'y':
        os.system("pkexec python3 /tmp/fedora-postinstall-config/scripts/dnf-fast.py")
        print(" dnf bylo úspěšně zrychleno")
    if codecs == 'n':
        print("instalace kodeků: přeskakuji.")
    elif codecs == 'Y' or 'y':
        os.system("sudo dnf groupupdate -y multimedia --setop='install_weak_deps=False' --exclude=PackageKit-gstreamer-plugin > /dev/null 2>&1 && sudo dnf groupupdate -y sound-and-video > /dev/null 2>&1")
    print('\033[1m' + 'post-konfigurace Fedory proběhla úspěšně!' + '\033[0m')
