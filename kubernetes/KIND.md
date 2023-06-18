See [](curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64)

The following are instructions from [Installing From Release Binaries](https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries)
on installing `kind` for the `x86_64` architecture:

```bash
# For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
# make executable
chmod +x ./kind
# move binary to /usr/local/bin
sudo mv ./kind /usr/local/bin/kind
```

Before making a cluster, have a look at the `K8s` [releases](https://kubernetes.io/releases/) page
to see which is the latest version of `k8s`. That is
in order to choose the most appropriate version to use
as basis.

Then head to [kindest/node](https://hub.docker.com/r/kindest/node)
on DockerHub to see if a container with that version is available.

Finally, update the `kind.yml` config file and create a
cluster by running the following command from within
the folder where `kind.yml` is located:

```bash
kind create cluster --config=kind.yml
```
This has the following output

```bash
Creating cluster "tkb" ...
 ✓ Ensuring node image (kindest/node:v1.27.2) 🖼 
 ✓ Preparing nodes 📦 📦 📦 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
 ✓ Joining worker nodes 🚜 
Set kubectl context to "kind-tkb"
You can now use your cluster with:

kubectl cluster-info --context kind-tkb

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
```

Verify the cluster was created successfully:

```bash
kind get clusters
# tkb
```
Check that you kubectl context is correctly set to your KinD `tkb` cluster: 
```bash
kubectl get nodes
```
