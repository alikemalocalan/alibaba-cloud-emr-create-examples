#!/usr/bin/env python
# coding=utf-8

import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408.CreateClusterV2Request import CreateClusterV2Request

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'eu-central-1', timeout=40, max_retry_time=5)

request = CreateClusterV2Request()
request.set_accept_format('json')

request.set_ZoneId("eu-central-1a")
request.set_SecurityGroupName("emr-security-group")
request.set_ChargeType("PostPaid")
request.set_VSwitchId("vsw-gw8ue96459069ui8pl8pc")
request.set_KeyPairName("alibaba-de")
request.set_VpcId("vpc-gw8b865ld4labpkquw3di")
request.set_NetType("vpc")
request.set_EmrVer("EMR-3.18.1")
request.set_ClusterType("HADOOP")
request.set_Name("test-cluster")
request.set_HostGroups([
    {
        "HostGroupType": "MASTER",
        "NodeCount": "1",
        "InstanceType": "ecs.sn2.large",
        "DiskType": "CLOUD_EFFICIENCY",
        "DiskCapacity": "80",
        "DiskCount": "1"
    },
    {
        "HostGroupType": "CORE",
        "NodeCount": "2",
        "InstanceType": "ecs.sn2.large",
        "DiskType": "CLOUD_EFFICIENCY",
        "DiskCapacity": "80",
        "DiskCount": "4"
    }
])

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
