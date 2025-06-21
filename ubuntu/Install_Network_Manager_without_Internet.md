## Network Manager not available

On a system with internet access:

```bash
mkdir network-manager-debs
cd network-manager-debs
apt download dns-root-data dnsmasq-base libbluetooth3 libndp0 libnm0 libteamdctl0 network-manager network-manager-pptp ppp pptp-linux
```

but the following is more reliable in case the package dependencies change in the meantime:

```bash
sudo apt install --download-only network-manager
```

This will put all `.deb` files into `/var/cache/apt/archives/`.

Copy those `.deb` files to a USB stick or other media.

Then on the system without internet access, mount the USB, navigate to `network-manager-debs` (if you need to, copy it to the home folder) and do:

```bash
cd ~/network-manager-debs
sudo dpkg -i *.deb
```

Then:

```bash
sudo systemctl enable NetworkManager
sudo systemctl start NetworkManager
```

Check it's running:

```bash
nmcli d
```

should return something along the lines of:

```bash
DEVICE        TYPE      STATE                   CONNECTION 
wlo1          wifi      disconnected            --
p2p-dev-wlo1  wifi-p2p  disconnected            --         
eno2          ethernet  unavailable             --         
```

You can also perform a restart (for example `sudo systemctl reboot`) if the service didn't start properly.

Finally, connect to a WiFi network as shown above:

```bash
nmcli d wifi connect my_wifi password <password>
```