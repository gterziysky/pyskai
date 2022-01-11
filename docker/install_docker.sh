
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# How to install docker image without access to docker.com
# https://stackoverflow.com/questions/37905763/how-do-i-download-docker-images-without-using-the-pull-command#41099881
# docker save command manual
# https://docs.docker.com/engine/reference/commandline/save/#cherry-pick-particular-tags
# docker load command manual
# https://docs.docker.com/engine/reference/commandline/load/#examples

# install docker from .deb packages
# download latest version from here:
# https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/

# see this post for more info on the docker .deb packages:
# # https://stackoverflow.com/questions/58741267/containerd-io-vs-docker-ce-cli-vs-docker-ce-what-are-the-differences-and-what-d

# Follow below order of installation

# 1. install containerd.io
sudo dpkg -i containerd.io_1.4.12-1_amd64.deb 
#Selecting previously unselected package containerd.io.
#(Reading database ... 108188 files and directories currently installed.)
#Preparing to unpack containerd.io_1.4.12-1_amd64.deb ...
#Unpacking containerd.io (1.4.12-1) ...
#Setting up containerd.io (1.4.12-1) ...
#Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /lib/systemd/system/containerd.service.
#Processing triggers for man-db (2.9.1-1) ...

# 2. install docker-ce-cli
sudo dpkg -i docker-ce-cli_20.10.11_3-0_ubuntu-focal_amd64.deb 
#Selecting previously unselected package docker-ce-cli.
#(Reading database ... 108204 files and directories currently installed.)
#Preparing to unpack docker-ce-cli_20.10.11_3-0_ubuntu-focal_amd64.deb ...
#Unpacking docker-ce-cli (5:20.10.11~3-0~ubuntu-focal) ...
#Setting up docker-ce-cli (5:20.10.11~3-0~ubuntu-focal) ...
#Processing triggers for man-db (2.9.1-1) ...

# 3. install from .deb packages
sudo dpkg -i docker-ce_20.10.11_3-0_ubuntu-focal_amd64.deb 
#Selecting previously unselected package docker-ce.
#(Reading database ... 108390 files and directories currently installed.)
#Preparing to unpack docker-ce_20.10.11_3-0_ubuntu-focal_amd64.deb ...
#Unpacking docker-ce (5:20.10.11~3-0~ubuntu-focal) ...
#Setting up docker-ce (5:20.10.11~3-0~ubuntu-focal) ...
#Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service.
#Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /lib/systemd/system/docker.socket.
#Processing triggers for systemd (245.4-4ubuntu3.13) ...

# run docker
# sudo docker run ubuntu
# sudo docker run -t -i --rm ubuntu bash
