#!/usr/bin/env python
import argparse
import boto3
import logging
import os
import re
import time
import urllib.request
import base64
import sys
import datetime


def query_instance(instance_name):
    existing_reservation = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])
    existing_reservation = existing_reservation['Reservations'][0]
    instance = existing_reservation['Instances'][0]

    return instance


def get_machine_public_ip():
    """
    Get the public IP address of the current machine.

    Returns:
         str: The public IP address of the current machine.
    """
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    # https://www.regular-expressions.info/ip.html
    regex = re.compile(pattern=r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    assert regex.match(string=external_ip) is not None, "Not a valid IP address. Please check the IP address lookup service"
    return external_ip


if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser()

    parser.add_argument("-in", "--instance_name", help="the name of the EC2 instance", default='dev-instance-1')
    args = parser.parse_args()

    instance_name = args.instance_name

    m = re.search(pattern=r'.*?(\d{1,})$', string=instance_name)
    if m is None:
        err_msg = "Please provide a numeric suffix at the end of the instance name."
        logger.error(err_msg)
        raise ValueError(err_msg)

    in_suffix = m.group(1)
    # other input params

    vol_name = 'dev-instance-ebs-%s' % in_suffix  # EBS vol name
    iam_role_name = "EC2_dev_role"  # apply an IAM role to the instance
    # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
    # before using a different zone, make sure the IAM role and security group exist, i.e. for 'us-east-1a'
    availability_zone = 'eu-central-1a'  # 'eu-central-1a', 'eu-central-1b'

    git_token = os.getenv('GIT_OAUTH_TOKEN', None)
    if git_token is None:
        err_msg = "Environment variable GIT_OAUTH_TOKEN is missing. " \
                  "For more information see https://help.github.com/en/articles/git-automation-with-oauth-tokens"
        logger.error(err_msg)
        raise ValueError(err_msg)

    # location of the bash script which sets up the machine
    user_data_script = "./setup_ec2_instance.sh"

    with open(user_data_script, 'r') as f:
        txt = f.read()
    # plug in the Git token and PG DB password

    # TODO: going forward, those two should be read from the AWS parameter store
    txt = txt.replace('GIT_PERSONAL_ACCESS_TOKEN_PLACEHOLDER', git_token)
    user_data_script = txt.replace('PUBLIC_IP_ADDRESS_OF_COMPUTER_USED_TO_EXECUTE_THE_SCRIPT', get_machine_public_ip())

    # remove all comments other than the shebang
    # user_data_script = re.sub(pattern="#(?!\!).*?\n", repl="", string=user_data_script)
    # remove all comments including the shebang
    user_data_script = re.sub(pattern="#.*?\n", repl="", string=user_data_script)
    # 1. Execute the script within a sudo command in order to run as the non-root user (by default cloud init scripts are
    # run as root).
    # 2. Enclose the commands within single quotes ' ' and prefix with a $-sign. The $ allows us to have single quotes
    # within the commands provided they are escaped, i.e. \'. This is the only way to change the postgres user password.
    # https://stackoverflow.com/questions/8254120/how-to-escape-a-single-quote-in-single-quote-string-in-bash/26165123#answer-8254156
    user_data_script = "#!/bin/bash\nsudo -H -u ubuntu /bin/bash -c $'%s'" % user_data_script

    # Standard Base64 Encoding
    encodedBytes = base64.b64encode(user_data_script.encode("utf-8"))
    # Base64 encoded UserData script
    user_data_script = str(encodedBytes, "utf-8")

    ec2 = boto3.client('ec2')
    # Ubuntu 20.04 LTS image
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances
    # datetime.datetime(2020, 7, 24, 12, 13, 14)

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_instances
    # TODO: get the spot price from the API
    #       https://aws.amazon.com/about-aws/whats-new/2017/04/use-the-enhanced-aws-price-list-api-to-access-aws-service-and-region-specific-product-and-pricing-information/
    #       https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html
    reservation = ec2.request_spot_instances(
        BlockDurationMinutes=180,  # how many minutes will the instance run before being terminated
        DryRun=False,
        SpotPrice='0.20', # 0.20
        Type='one-time',
        InstanceCount=1,
        # specify a small time frame for the request in order to have it fail soon
        # default request lifetime is 7 days
        ValidFrom=datetime.datetime.utcnow() + datetime.timedelta(seconds=5),
        ValidUntil=datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        # TagSpecifications=[
        #     {'ResourceType': 'instance',
        #      'Tags': [
        #         {
        #             'Key': 'Name',
        #             'Value': instance_name
        #         }
        #     ]
        #     }
        # ],
        LaunchSpecification={
            # ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20200716 - ami-079024c517d22af5b
            'ImageId': 'ami-079024c517d22af5b',
            'KeyName': 'GalenMBP',
            'SecurityGroups': ['ssh-access-limit'],
            'InstanceType': 'g4dn.xlarge',  # 'g2.2xlarge',  # 'g4dn.xlarge', 'p2.xlarge'
            'Placement': {
                'AvailabilityZone': availability_zone,
            },
            'IamInstanceProfile': {'Name': iam_role_name},
            'UserData': user_data_script,
            'BlockDeviceMappings': [
                {
                    'DeviceName': "/dev/sda1",
                    'Ebs': {
                        # 'SnapshotId': 'snap-f70deff0',
                        'VolumeSize': 20,
                        'DeleteOnTermination': True,
                        'VolumeType': 'gp2',
                        # 'Iops': 300,
                        # 'Encrypted': False
                    },
                },
            ],
            # 'EbsOptimized': True,

            # 'Monitoring': {
            #     'Enabled': True
            # },
            'SecurityGroupIds': [
                'sg-0aca069fbc378e459',
            ],
        }
    )

    # reservation['SpotInstanceRequests'][0]['State']
    # 'SpotInstanceRequestId'
    # instance = reservation['Instances'][0]
    spot_inst_req_id = reservation['SpotInstanceRequests'][0]['SpotInstanceRequestId']

    logger.info("Waiting a bit for the the request to get registered...")
    time.sleep(2)

    res = ec2.describe_spot_instance_requests(
        DryRun=False,
        SpotInstanceRequestIds=[
            spot_inst_req_id
        ]
    )

    while 'fulfilled' != res['SpotInstanceRequests'][0]['Status']['Code']:
        res = ec2.describe_spot_instance_requests(
            DryRun=False,
            SpotInstanceRequestIds=[
                spot_inst_req_id
            ]
        )
        logger.info("Request Status last updated %s\nStatus code: %s\nStatus message: %s\nRequest created at %s\nRequest expires at %s",
                    res['SpotInstanceRequests'][0]['Status']['UpdateTime'].strftime("%Y-%m-%d %H:%M:%S UTC"),
                    res['SpotInstanceRequests'][0]['Status']['Code'],
                    res['SpotInstanceRequests'][0]['Status']['Message'],
                    res['SpotInstanceRequests'][0]['CreateTime'].strftime("%Y-%m-%d %H:%M:%S UTC"),
                    res['SpotInstanceRequests'][0]['ValidUntil'].strftime("%Y-%m-%d %H:%M:%S UTC"))

        if res['SpotInstanceRequests'][0]['Status']['Code'] in ['capacity-not-available', 'price-too-low', 'constraint-not-fulfillable']:
            # exit if our bid price is lower than the minimum spot price for the instance
            # see
            # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#using-spot-instances-managing-interruptions
            sys.exit(0)
        time.sleep(10)

    if 'InstanceId' in res['SpotInstanceRequests'][0].keys():
        # at this point we already have an instance ID
        instance_id = res['SpotInstanceRequests'][0]['InstanceId']
    else:
        logger.info("Instance reservation failed.")
    # create a human-friendly name for the instance
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_tags
    # tag the image
    ct_res = ec2.create_tags(Resources=[instance_id],
                             Tags=[{'Key': 'Name', 'Value': instance_name}])

    # # wait for the VolumeId to become available
    # while len(instance['BlockDeviceMappings']) == 0:
    #     logger.info("No device is attached to the instance yet. Waiting for the instance to become available...")
    #     time.sleep(10)
    #     instance = query_instance(instance_name=instance_name)
    #
    # vol_id = instance['BlockDeviceMappings'][0]['Ebs']['VolumeId']
    #
    # # create a human-friendly name for the volume
    # res = ec2.create_tags(Resources=[vol_id],
    #                       Tags=[{'Key': 'Name', 'Value': vol_name}])

    # wait until the EC2 instance is up and running
    instance = query_instance(instance_name=instance_name)
    # while 'PublicDnsName' not in instance.keys() or instance['PublicDnsName'] == '':
    while instance['State']['Name'] == 'running':
        logger.info("Instance state: %s. Waiting for the instance to become available...", instance['State']['Name'])
        time.sleep(10)
        instance = query_instance(instance_name=instance_name)

    # at this point the public DNS should already be available
    logger.info("Instance state: %s; Public DNS: %s", instance['State']['Name'], instance['PublicDnsName'])
    logger.info("To ssh into the machine do:\nssh -i ~/.ssh/id_rsa ubuntu@%s", instance['PublicDnsName'])
