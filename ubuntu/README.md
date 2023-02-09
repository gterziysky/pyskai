### Instructions
* [Enable Wake-on-LAN for Ubuntu](https://www.maketecheasier.com/enable-wake-on-lan-ubuntu/)
* [Ubuntu Wake on LAN](https://help.ubuntu.com/community/WakeOnLan)
* [Enable Wake on LAN feature](https://www.golinuxcloud.com/wake-on-lan-ubuntu/#Enable_Wake_on_Lan_Feature)
* [Wake on LAN persistance](https://ubuntu-mate.community/t/wake-on-lan-persistance-issues-22-04/25600/2)
* [Send magic packet from Mac OS](https://apple.stackexchange.com/questions/95246/wake-other-computers-from-mac-osx#229596)

First, enable WOL in your BIOS. For instructions, look up your motherboard's manual

Install ethtool
```bash
sudo apt-get install ethtool
```

Check the identifier of your NIC - look for the one with the IP address
```bash
ip a
```

Assuming the name of your NIC is `enp5s0`, check if WoL is enabled you should see `Wake-on: g` if it is enabled and `Wake-on: d` if it isn't.

```bash
sudo ethtool enp5s0 | grep Wake
```

To enable WoL:
```bash
sudo ethtool -s enp5s0 wol g
```

To persist WoL on system restart, create a service
```bash
cd ~

echo -e "[Unit]\nDescription=Enable Wake-up on LAN\n\n[Service]\nType=oneshot\nExecStart=$(which ethtool) -s enp5s0 wol g\n\n[Install]\nWantedBy=basic.target" > wol-enable.service

sudo cp wol-enable.service /etc/systemd/system
```

Refresh systemctl:
```bash
sudo systemctl daemon-reload

sudo systemctl start wol-enable.service 
sudo systemctl enable wol-enable.service
```

You should see the following output
```bash
Created symlink /etc/systemd/system/basic.target.wants/wol-enable.service → /etc/systemd/system/wol-enable.service.
```

Check status
```bash
systemctl status wol-enable
```

On your local machine (assuming it is a Mac) do:
```bash
brew install wakeonlan
```

Then:
```bash
# wakeonlan -i BROADCAST_ADDR -p PORT TARGET_MAC_ADDRESS
wakeonlan -i 192.168.1.255 -p 9 01:02:03:04:05:06 # MAC address of NIC
# or, equivalently, when the default port is 9:
wakeonlan -i 192.168.1.255 01:02:03:04:05:06 # MAC address of NIC
```

To wake up using TeamViewer, go to Extras -> Options and under the General tab, locate Wake-on-LAN
Click Configure, then select option "Other TeamViewer within your local network".
Enter the TeamViewer ID of the computer which will be used to wake up the remote computer.
Make sure incoming connections is set to accept.


Next, follow [installing conda in silent mode](https://docs.anaconda.com/anaconda/install/silent-mode/).

Install pytorch:
```bash
conda create --name mlenv --yes python=3.10 pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
```

Install additional packages:
```bash
conda install --channel conda-forge --yes pandas notebook scikit-learn
```

### Reverse ssh

[Guide on reverse SSH](0~https://www.howtogeek.com/428413/what-is-reverse-ssh-tunneling-and-how-to-use-it/)
