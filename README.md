```shell script
=============================
                 _         _
 _ __  _   _ ___| | ____ _(_)
| '_ \| | | / __| |/ / _` | |
| |_) | |_| \__ |   | (_| | |
| .__/ \__, |___|_|\_\__,_|_|
|_|    |___/
=============================
```

```shell script
# start PyCharm
aws-vault exec aws.profile --duration=1h -- /Applications/PyCharm\ CE.app/Contents/MacOS/pycharm

# create an ec2 instance - with at least 12 GiB storage
aws-vault exec aws.profile -- python ./create_ec2_instance.py -in dev-instance-3

# copy files to the instance
scp -i ~/.ssh/id_rsa ~/path/to/file/NNet.ipynb ubuntu@EC2_INSTANCE_PUB_DNS:/home/ubuntu/
```
