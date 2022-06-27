git clone https://github.com/vikdevelop/fedora-postinstall-config /tmp/fedora-postinstall-config 
cd /tmp/fedora-postinstall-config
echo "Tento skript vyžaduje prává uživatele superuser. Pro pokračování zadejte heslo:"
sudo python3 fedora-postinstall-config 
cd 
rm -rf /tmp/fedora-postinstall-config
