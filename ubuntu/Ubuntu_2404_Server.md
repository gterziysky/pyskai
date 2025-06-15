## Ubuntu 24.04 LTS Server install guides:
* [how to install ubuntu server](https://www.linuxtechi.com/how-to-install-ubuntu-server/#8_Disk_Partitioning) - recommended guide
* [official guide](https://ubuntu.com/tutorials/install-ubuntu-server#11-confirm-changes)

Make sure to [edit the GRUB file accordingly](https://github.com/gterziysky/pyskai/blob/master/ubuntu/ASUS_Pro_WS_WRX80E_SAGE_SE_WIFI.md).

For configuring WiFi post install, see [Configure WiFi Connections](https://ubuntu.com/core/docs/networkmanager/configure-wifi-connections).

```bash
# HINT: nmcli is in the network-manager package
sudo apt-get update && sudo apt-get install network-manager
# Then run
nmcli d wifi connect my_wifi password <password>
```

### Resize default LVM partition
To resize the Default LVM partition postinstall, see the following guide: [How to Extend the Default Ubuntu LVM Partition](https://packetpushers.net/blog/ubuntu-extend-your-default-lvm-space/).


## Install Nvidia drivers

See section **A note about ubuntu-drivers command-line method # 3** in [Ubuntu Linux Install Nvidia Driver (Latest Proprietary Driver)](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/).

### Install the Nvidia container toolkit

For more information, refer to [docker/install_docker_and_nvidia_container_toolkit.md](https://github.com/gterziysky/pyskai/blob/master/docker/install_docker_and_nvidia_container_toolkit.md).

Additional resources:
* [NVIDIA : Install Container Toolkit](https://www.server-world.info/en/note?os=Ubuntu_24.04&p=nvidia&f=3)
* The official docs here - [installing with Apt](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt)

If all docker commands hang (`docker ps`, `docker image list`, etc.), containerd (`/etc/containerd/configtoml`) and/or docker (`/etc/docker/daemon.json`) may be improperly configured.

See [Configuring Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker) and run the instructions to update the `/etc/docker/daemon.json` file.

Similarly, check [configuring containerd (for Kubernetes)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-kubernetes) for containerd.

### How to solve flickering screen during Ubuntu 24.04 LTS Server installation

**TL;DR**

At the `Try or Install Ubuntu Server`, edit the Grub config and add `nomodeset` at the line starting with `linux` like below:

```shell
# ...
linux   /casper/vmlinuz nomodeset ---
# ...
```

After the Nvidia drivers are installed, the problem goes away.

To solve a flickering screen during the installation of Ubuntu 24.04 LTS, you can try the following methods:

1. Boot with Safe Graphics Mode
On the installation menu, press e to edit the boot parameters.
Find the line starting with linux and add nomodeset at the end.
Press F10 to boot with these options. This may help with display issues.

2. Use a Different Video Driver
If you're using an NVIDIA or AMD GPU, you might need to install proprietary drivers later. For now, using nomodeset can help you complete the installation, after which you can install the appropriate drivers.

3. Check Your Hardware Connections
Ensure that all cables and connections are secure. A loose cable can sometimes cause screen flickering.

4. Try a Different Display Resolution
Sometimes, a compatible resolution can help. After installation, you can adjust the display settings in Ubuntu.

5. Use Alternate Installation Media

If the issue persists, try using a different USB drive or DVD to create the installation media, as corruption can lead to display problems.

Summary
These methods should help resolve flickering issues during installation. If the problem continues, consider checking compatibility with your hardware or seeking help on forums for specific troubleshooting.

Links:
* [Manual "nomodeset" Kernel Boot Line Option for Linux Booting](https://www.dell.com/support/kbdoc/en-us/000123893/manual-nomodeset-kernel-boot-line-option-for-linux-booting)
* [What does nomodeset do?](https://www.reddit.com/r/Ubuntu/comments/1i7kps/what_does_nomodeset_do/)
* [Ubuntu_grub.cfg](https://github.com/rutgerblom/ubuntu-autoinstall/blob/2690adf4268818806d2638782bc661e1e9d8e0b1/Ubuntu_grub.cfg#L15)