Instructions from the official docker documentation: [Install using the apt repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

## Uninstall old versions
Before you can install Docker Engine, you need to uninstall any conflicting packages.

Your Linux distribution may provide unofficial Docker packages, which may conflict with the official packages provided by Docker. You must uninstall these packages before you install the official version of Docker Engine.

The unofficial packages to uninstall are:

```bash
docker.io
docker-compose
docker-compose-v2
docker-doc
podman-docker
```

Moreover, Docker Engine depends on containerd and runc. Docker Engine bundles these dependencies as one bundle: containerd.io. If you have installed the containerd or runc previously, uninstall them to avoid conflicts with the versions bundled with Docker Engine.

Run the following command to uninstall all conflicting packages:

```bash
 for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
 ```
apt-get might report that you have none of these packages installed.

Images, containers, volumes, and networks stored in /var/lib/docker/ aren't automatically removed when you uninstall Docker. If you want to start with a clean installation, and prefer to clean up any existing data, read the uninstall Docker Engine section.

## Install using the `apt` repo

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install the docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Create a docker group
```bash
sudo groupadd docker
# Add your user to the docker group.
sudo usermod -aG docker $USER
```

Log out and log back in so that your group membership is re-evaluated.

## Install nvidia-container-toolkit

See [NVIDIA : Install Container Toolkit](https://www.server-world.info/en/note?os=Ubuntu_24.04&p=nvidia&f=3) as well as the official docs here [Installing with Apt](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt).

Make sure to run the following sections:
- [Configuring docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-docker)
- [Configuring containerd (for Kubernetes)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuring-containerd-for-kubernetes)

## Uninstall docker

```bash
for pkg in docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin; do sudo apt-get remove $pkg; done
```

## Uninstall nvidia container toolkit

```bash
for pkg in libnvidia-container-tools libnvidia-container1 nvidia-container-toolkit nvidia-container-toolkit-base; do sudo apt-get remove $pkg; done
```

## References

See [NVIDIA : Install Container Toolkit](https://www.server-world.info/en/note?os=Ubuntu_24.04&p=nvidia&f=3)
