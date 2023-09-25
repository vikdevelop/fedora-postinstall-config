# fedora-postinstall-config
This simple Python script allows you to post installation configuration your Fedora distribution. This includes checking for updates after installing the system, setting up GRUB + Btrfs and installation Timeshift, adding the Flathub repository, installing recommended Flatpak apps, setting up codecs, speeding up DNF package manager and installation useful software for settings your graphic card.

### Installation
```bash
wget -qO /tmp/installation.sh https://raw.githubusercontent.com/vikdevelop/fedora-postinstall-config/main/installation.sh && sh /tmp/installation.sh
```
