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


if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    ec2 = boto3.client('ec2')

    res = ec2.describe_spot_instance_requests(
        Filters=[
            # {
            #     "Name": "availability-zone-group",
            #     "Values": [
            #         'eu-central-1a'
            #     ]
            # },
            # {
            #     "Name": "launch.group-id",
            #     "Values": [
            #         'security group id'
            #     ]
            # },
            # {
            #     "Name": "launch.key-name",
            #     "Values": [
            #         'key pair name'
            #     ]
            # },
            {
                "Name": "state",
                "Values": [
                    'open'
                ]
            },
        ],
        DryRun=False
    )
    sir_to_cancel = []
    for sir in res['SpotInstanceRequests']:
        if sir['State'] == 'open':
            logger.info("Adding open request %s with ttl [%s; %s] to the cancellation list.",
                        sir['SpotInstanceRequestId'],
                        sir['CreateTime'].strftime("%Y-%m-%d %H:%M:%S UTC"),
                        sir['ValidUntil'].strftime("%Y-%m-%d %H:%M:%S UTC"))
            sir_to_cancel.append(sir['SpotInstanceRequestId'])

    res2 = ec2.cancel_spot_instance_requests(SpotInstanceRequestIds=sir_to_cancel)

    logger.info("%s", str(res2))
