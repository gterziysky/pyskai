Prevent power off at login screen after inactivity:

```shell
sudo nano /etc/systemd//logind.conf
# Scroll down to section [Login]
# Set IdleAction=ignore
# exit file
# restart systemd login daemon service
sudo systemctl restart systemd-logind
# This will log you out so you would need to log nack in
```
