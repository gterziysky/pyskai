## Connecting to WiFi on Ubuntu Server (without NetworkManager)

Ubuntu Server 26.04 uses `systemd-networkd` combined with `Netplan` to handle network configuration, which is standard for headless, stable server environments.

The default behavior is that `Netplan` reads YAML files in `/etc/netplan/` to configure network interfaces through `systemd-networkd`. While NetworkManager is the default network renderer for Ubuntu Desktop 26.04, not the Server edition.

NetworkManager is not recommended for traditional server setups.

Netplan is recommended for modern Ubuntu Server. Netplan is the default network configuration tool on Ubuntu Server.

1. Identify your wireless interface

```bash
ip link show
# or
iw dev
```
Usually named wlan0, wlp2s0, or similar.

2. Create/edit Netplan configuration

```bash
sudo nano /etc/netplan/00-wifi-config.yaml
```

3. Add WiFi configuration

```yaml
network:
  version: 2
  renderer: networkd
  wifis:
    wlan0:          # Replace with your interface name
      dhcp4: true
      access-points:
        "YourNetworkName":
          password: "YourPassword"
```

For static IP:
```yaml
network:
  version: 2
  renderer: networkd
  wifis:
    wlan0:
      dhcp4: false
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      access-points:
        "YourNetworkName":
          password: "YourPassword"
```

4. Apply the configuration

```bash
sudo netplan generate
sudo netplan apply
```

## How to install Network Manager without internet access

If you do prefer to use NetworkManager you can install it on Ubuntu Server.

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