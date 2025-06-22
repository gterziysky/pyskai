## Install

Check available releases:

```bash
snap info microk8s
```

Once a release has been chose, pass it onto the `--channel` parameter:

```bash
sudo snap install microk8s --classic --channel=1.33
```

Join the microk8s group, create the `~/.kube` folder and set permissions:

```bash
sudo usermod -a -G microk8s $USER
mkdir -p ~/.kube
chmod 0700 ~/.kube
```

You need to log out and log back in in order for the changes in groups to take effect.

## Uninstall Microk8s

The [cleanest way](https://blog.duaneleem.com/uninstall-microk8s-ubuntu-22-04-2-lts/) to remove Microk8s is:

```bash
sudo microk8s reset # <-- this command can take several minutes
sudo snap remove microk8s
```
