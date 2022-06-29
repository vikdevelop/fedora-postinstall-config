# fedora-postinstall-config
## EN
This simple Python script allows you to post installation configuration your Fedora distribution. This includes checking for updates after installing the system, setting up GRUB + Btrfs and installation Timeshift, adding the Flathub repository, installing recommended Flatpak apps, setting up codecs, speeding up DNF package manager and installation useful software for settings your graphic card.

## CZ
Tento jednoduchý skript v Pythonu umožňuje provést po-instalační konfiguraci distribuce Fedora. To zahrnuje kontrolu aktualizací po instalaci systému, nastavení GRUB + Btrfs a instalace Timeshift, přidání Flathub repositáře, instalace doporučených aplikací Flatpak, nastavení kodeků, zrychlení správce balíčků DNF a instalaci užitečného softwaru pro nastavení vaší grafické karty.

### Installation
```bash
wget -qO /tmp/installation.sh https://raw.githubusercontent.com/vikdevelop/fedora-postinstall-config/main/installation.sh && sh /tmp/installation.sh
```
