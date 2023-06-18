Docker compose V2 is available with Docker Desktop.

If a standalone installation is needed (i.e. if Docker was not installed with Docker Desktop), see
[Scenario three: Install the Compose standalone](https://docs.docker.com/compose/install/#scenario-three-install-the-compose-standalone)

Concrete instructions are available at [Install Compose standalone](https://docs.docker.com/compose/install/standalone/):

```bash
cd ~/Downloads
curl -SL https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-linux-x86_64 -o ~/Downloads/docker-compose
chmod +x docker-compose
sudo mv docker-compose /usr/local/bin/docker-compose
```

