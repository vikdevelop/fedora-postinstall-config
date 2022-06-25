# fedora-postconfig
## CZ:
Tento jednoduchý skript v Pythonu umožňuje provést post-konfiguraci distribuce Fedora. To zahrnuje kontrolu aktualizací po instalaci systému, nastavení GRUB + Btrfs, přidání Flathub repositáře, instalace Flatpak a DNF aplikací (uživatel si vybere které aplikace chce nainstalovat), nastavení kodeků a dobrovolnou instalaci proprietárních ovladačů nVidia.
### Instalace
```bash
wget -qO /tmp/fedora-postconfig https://raw.githubusercontent.com/vikdevelop/fedora-postconfig/main/fedora-postconfig && python3 /tmp/fedora-postconfig
```
## EN
This simple Python script allows you to post-configure your Fedora distribution. This includes checking for updates after installing the system, setting up GRUB + Btrfs, adding the Flathub repository, installing Flatpak and DNF applications (the user chooses which applications they want to install), setting up codecs, and optionally installing proprietary nVidia drivers.
### Installation
```bash
wget -qO /tmp/fedora-postconfig https://raw.githubusercontent.com/vikdevelop/fedora-postconfig/main/fedora-postconfig && python3 /tmp/fedora-postconfig
```
