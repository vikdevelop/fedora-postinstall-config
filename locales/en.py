#!/usr/bin/python3
# English translations of Fedora-postinstall-config

# Begin
checking = '→ checking if it is a Fedora distribution '
xerror = 'it looks like the Fedora distribution is not installed on this HW, or it is corrupted. In this case, you cannot use this script :('
sudo = '→→ we will now ask you for your password within sudo that choosed in installation of Fedora, because we need to update the Fedora distribution packages to the latest version:'
update_status = '→ updatation Fedory '

# Summary
summary_title = "Summary: "
summary_description = "- checking name of distro - OK \n- updatation of Fedora - OK \n- configuration GRUB + Btrfs a installation timeshift \n- configuration Flathub repository and installation recommended Flatpak apps \n- configuration of codecs \n- speeding up DNF \n- installation optional SW for your graphic card"
continueyn = "Would you like to continue? [Y/n]: "
canceled = "Canceled."

# GRUB-BTRFS configuration
grub_btrfs_title = "→ configuration GRUB + Btrfs"
timeshift_make = "→→ checking if is installed timehift and make"
grub_btrfs_downloading = "→→ downloading repository grub-brtfs"
download_folder = "Downloads"
make_status = "→→→ compilation & installation with program make was successfull"
grub_btrfs_status = "→→ configuration GRUB + Btrfs was successfull"
grub_btrfs_already_configured = "→ GRUB + Btrfs already configured."

# Flatpak + Flathub configuration
flathub_repo_status = "→ adding Flathub repository"
flatpak_installation_title = "→ installation recommended Flatpak apps"
flatpak_installation_desc = "If you want, you can skip this step by pressing the enter key (press the c key to continue): "
skip_flatpakinstall = "installation Flatpak apps: I skiping."
flatseal = "Do you want install the Flatseal app that allows you to set permissions on Flatpak apps? [Y/n]: "
em = "Do you want to install the Extension Manager application that allows you to manage extensions for GNOME (Fedora Workstation edition)? [Y/n]: "
dw = "Do you want to install Dynamic Wallpaper, an application that allows you to set transient wallpapers in GNOME? [Y/n]: "
flatseal_installed_status = "Flatseal already installed."
em_installed_status = "Extension Manager already installed."
dw_installed_status = "Dynamic Wallpaper already installed."

# Multimedia codecs configuration
media_codecs_title = "→ multimedia codecs"
media_codecs_desc = "→→ sometimes you may encounter potential problems with codecs in the web browser (but also in other applications)."
codecs_input = "→→→ so do you wish to install additional multimedia codecs? [Y/n]:  "
skip_codecs_installation = "installation codecs: I skiping."

# DNF speed up
dnf_speedup_title_desc = "→ speeding up DNF pkg manager \n→→ DNF package manager is one of the slower package managers. However, it is possible to speed it up."
dnf_input = "→→→ so do you wish speeding up dnf pkg manager? [Y/n]: "
skip_dnf_speedup = "speeding up dnf: I skiping."
dnf_speedup_successfull = " dnf was speed up successfull."

# GPU configuration -NVIDIA
nvidiagpu_installation_title = "→ installation proprietary driver by nVidia"
nvidiagpu_installation_input = "→→ do you wish install proprieaty driver by nVidia? [Y/n]: "
nvidiagpu_skip = "installation nVidia driver - I skiping."
update_before_installation_nvidiagpu = "→ before installing a proprietary nVidia driver, we first check for other updates:"
nvidiagpu_installation_status = "→ installing proprietary nVidia Linux akmod graphic card driver:"
nvidiagpu_warning_restart = 'For your nVidia graphics card settings to take effect, you must restart your computer'
# Corectrl configuration -for AMD GPUs
corectrl_title = "→ installation program CoreCtrl for simple setting GPU by AMD"
corectrl_input = "→→ do you want intstall CoreCtrl? [Y/n]: "
corectrl_skip = "installation CoreCtrl: I skiping"
corectrl_status = 'CoreCtrl was instaled successfull'

# Message about successfully post-install configuration of Fedora
postinstall_config_successfull = 'post-install configuration of Fedora was successfull!'
