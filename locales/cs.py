#!/usr/bin/python3
# Czech translations of Fedora-postinstall-config

# Begin
checking = '→ kontrola, jestli se jedná o distribuci Fedora '
xerror = 'vypadá to, že na tomto HW není nainstalovaná distribuce Fedora, nebo je poškozená. V takovém případě nemůžete tento skript použít :('
sudo = '→→ nyní se vám zobrazí výzva pro zadání hesla, které jste zvolili při instalaci Fedory, protože je potřeba aktualizovat balíčky distribuce Fedora na nejnovější verzi:'
update_status = '→ aktualizace Fedory '

# Summary
summary_title = "Shrnutí: "
summary_description = "- kontrola názvu distribuce - OK \n- aktualizace systému - OK \n- konfigurace GRUB + Btrfs a instalace timeshift \n- konfigurace Flathub repositáře a instalace Flatpak aplikací \n- konfigurace kodeků \n- zrychlení DNF \n- instalace volitelného SW pro vaší grafickou kartu"
continueyn = "Chcete pokračovat? "
canceled = "Zrušeno."

# GRUB-BTRFS configuration
grub_btrfs_title = "→ konfigurace GRUB + Btrfs"
timeshift_make = "→→ kontrola jestli je nainstalován timehift a make"
grub_btrfs_downloading = "→→ stahování repozitáře grub-brtfs"
download_folder = "Stažené"
make_status = "→→→ kompilace a instalace pomocí programu make proběhla úspěšně"
grub_btrfs_status = "→→ konfigurace GRUB + Btrfs proběhla úspěšně"
grub_btrfs_already_configured = "→ GRUB + Btrfs již bylo nakonfigurováno."

# Flatpak + Flathub configuration
flathub_repo_status = "→ přidávání Flathub repositáře"
flatpak_installation_title = "→ instalace doporučených Flatpak aplikací"
flatpak_installation_desc = "Jestli chcete, můžete tento krok přeskočit stisknutím klávesy enter (pro pokračování stiskněte klávesu c): "
skip_flatpakinstall = "instalace Flatpak aplikací: přeskakuji."
flatseal = "Chcete nainstalovat aplikaci Flatseal, která umožňuje nastavovat oprávnění aplikací Flatpak? [Y/n]: "
em = "Chcete nainstalovat aplikaci Extension Manager, která umožňuje spravovat rozšíření pro prostředí GNOME (edice Fedora Workstation)? [Y/n]: "
dw = "Chcete nainstalovat aplikaci Dynamic Wallpaper (Dynamická tapeta), která umožňuje nastavování přechodných tapet v prostředí GNOME? [Y/n]: "
flatseal_installed_status = "Flatseal je již nainstalovaný."
em_installed_status = "Extension Manager je již nainstalovaný."
dw_installed_status = "Dynamic Wallpaper je již nainstalovaný."

# Multimedia codecs configuration
media_codecs_title = "→ multimediální kodeky"
media_codecs_desc = "→→ občas se můžete setkat s potenciálními problémy s kodeky ve webovém prohlížeči (ale i v jiných aplikacích)."
codecs_input = "→→→ přejete si tedy nainstalovat dodatečné multimediální kodeky? [Y/n]: "
skip_codecs_installation = "instalace kodeků: přeskakuji."

# DNF speed up
dnf_speedup_title_desc = "→ zrychlení správce balíčků DNF\n→→ DNF patří k těm pomalejším správcům balíčků. Je však možné ho zrychlit."
dnf_input = "→→→ přejete si tedy zrychlit správce balíčků dnf? [Y/n]: "
skip_dnf_speedup = "zrychlení dnf: přeskakuji."
dnf_speedup_successfull = " dnf bylo úspěšně zrychleno"

# GPU configuration -NVIDIA
nvidiagpu_installation_title = "→ instalace proprietárního ovladače od nVidie"
nvidiagpu_installation_input = "→→ přejete si nainstalovat proprietární ovladač pro GPU od nVidie? [Y/n]: "
nvidiagpu_skip = "instalace nVidia ovladačů - přeskakuji"
update_before_installation_nvidiagpu = "→ před instalací proprietárního ovladače nVidia nejdříve zkontrolujeme, zda nejsou k dispozici další aktualizace:"
nvidiagpu_installation_status = "→ instaluje se proprietární nVidia Linux akmod graphic card driver:"
nvidiagpu_warning_restart = 'Aby se nastavení vaší grafické karty od nVidie projevily, je nutné restartovat počítač'
# Corectrl configuration -for AMD GPUs
corectrl_title = "→ instalace programu CoreCtrl pro jednoduché nastavení GPU od AMD"
corectrl_input = "→→ chcete tedy nainstalovat program CoreCtrl? [Y/n]: "
corectrl_skip = "instalace corectrl: přeskakuji"
corectrl_status = 'CoreCtrl was instaled successfull'

# Message about successfully post-install configuration
postinstall_config_successfull = 'po-instalační konfigurace Fedory proběhla úspěšně!'
