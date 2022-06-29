#!/usr/bin/python3
# Deutch translations of Fedora-postinstall-config

# Begin
checking = '→ überprüfung, ob es sich um eine Fedora-Distribution handelt '
xerror = 'es sieht so aus, als ob die Fedora-Distribution auf dieser HW nicht installiert ist oder beschädigt ist. In diesem Fall können Sie dieses Skript nicht verwenden :('
sudo = '→→ wir werden Sie nun nach Ihrem Passwort für sudo fragen, das Sie bei der Installation von Fedora gewählt haben, da wir die Fedora-Distributionspakete auf die neueste Version aktualisieren müssen:'
update_status = '→ aktualisierung Fedora '

# Summary
summary_title = "zusammenfassung: "
summary_description = "- Überprüfung des Distro-Namens - OK \n- Aktualisierung von Fedora - OK \n- Konfiguration GRUB + Btrfs und Installation Timeshift \n- Konfiguration Flathub-Repository und Installation empfohlener Flatpak-Apps \n- Konfiguration von Codecs \n- Beschleunigung von DNF \n- Installation optionaler SW für Ihre Grafikkarte"
continueyn = "Möchten Sie fortfahren? [Y/n]: "
canceled = "Storniert."

# GRUB-BTRFS configuration
grub_btrfs_title = "→ konfiguration GRUB + Btrfs"
timeshift_make = "→→ prüfung, ob Timehift und Make installiert sind"
grub_btrfs_downloading = "→→ herunterladen des Repository grub-brtfs"
download_folder = "Downloads"
make_status = "→→→ kompilierung und Installation mit dem Programm make war erfolgreich"
grub_btrfs_status = "→→ konfiguration GRUB + Btrfs war erfolgreich"
grub_btrfs_already_configured = "→ GRUB + Btrfs bereits konfiguriert."

# Flatpak + Flathub configuration
flathub_repo_status = "→ hinzufügen Flathub repository"
flatpak_installation_title = "→ installation empfohlene Flatpak-apps"
flatpak_installation_desc = "Wenn Sie möchten, können Sie diesen Schritt durch Drücken der Enter überspringen (drücken Sie die Taste c, um fortzufahren): "
skip_flatpakinstall = "installation Flatpak apps: Ich Überspringen."
flatseal = "Willst du die Flatseal-App installieren, mit der du die Berechtigungen für Flatpak-Apps festlegen kannst? [Y/n]: "
em = "Möchten Sie die Anwendung Extension Manager installieren, mit der Sie Erweiterungen für GNOME (Fedora Workstation Edition) verwalten können? [Y/n]: "
dw = "Möchten Sie Dynamic Wallpaper installieren, eine Anwendung, mit der Sie vorübergehende Hintergrundbilder in GNOME einstellen können? [Y/n]: "
flatseal_installed_status = "Flatseal bereits installiert."
em_installed_status = "Extension Manager bereits installiert."
dw_installed_status = "Dynamic Wallpaper bereits installiert."

# Multimedia codecs configuration
media_codecs_title = "→ multimedia-codecs"
media_codecs_desc = "→→ manchmal kann es zu Problemen mit Codecs im Webbrowser (aber auch in anderen Anwendungen) kommen."
codecs_input = "→→→ möchten Sie also zusätzliche Multimedia-Codecs installieren? [Y/n]:  "
skip_codecs_installation = "installation codecs: Ich Überspringen."

# DNF speed up
dnf_speedup_title_desc = "→ beschleunigung von DNF pkg manager \n→→ DNF package manager ist einer der langsamsten Paketmanager. Es ist jedoch möglich, ihn zu beschleunigen."
dnf_input = "→→→ möchten Sie also den dnf pkg manager beschleunigen? [Y/n]: "
skip_dnf_speedup = "speeding up dnf: Ich Überspringen."
dnf_speedup_successfull = " dnf wurde erfolgreich beschleunigt."

# GPU configuration -NVIDIA
nvidiagpu_installation_title = "→ installation eines proprietären Treibers von nVidia"
nvidiagpu_installation_input = "→→ Möchten Sie einen proprietären Treiber von nVidia installieren? [Y/n]: "
nvidiagpu_skip = "installation nVidia driver - Ich Überspringen."
update_before_installation_nvidiagpu = "→ bevor wir einen proprietären nVidia-Treiber installieren, prüfen wir zunächst, ob es andere Updates gibt:"
nvidiagpu_installation_status = "→ Installation des proprietären nVidia Linux akmod graphic card driver:"
nvidiagpu_warning_restart = 'Damit die Einstellungen Ihrer nVidia-Grafikkarte wirksam werden, müssen Sie Ihren Computer neu starten'
# Corectrl configuration -for AMD GPUs
corectrl_title = "→ Installationsprogramm CoreCtrl zur einfachen Einstellung der GPU von AMD"
corectrl_input = "→→ Möchtest du installiere CoreCtrl? [Y/n]: "
corectrl_skip = "installation CoreCtrl: Ich Überspringen"
corectrl_status = 'CoreCtrl was instaled successfull'

# Message about successfully post-install configuration of Fedora
postinstall_config_successfull = 'Die Post-Installations-Konfiguration von Fedora war erfolgreich!'
