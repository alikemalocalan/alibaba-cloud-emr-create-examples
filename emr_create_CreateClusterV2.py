#!/usr/bin/env python
# coding=utf-8

import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408.CreateClusterV2Request import CreateClusterV2Request

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'eu-central-1', timeout=40, max_retry_time=5)

request = CreateClusterV2Request()
request.set_accept_format('json')

request.set_EasEnable(False)
request.set_IsOpenPublicIp(False)
request.set_SshEnable(True)
request.set_InstanceGeneration("ecs-3")
request.set_KeyPairName("alibaba-de")
request.set_Period(1)
request.set_MachineType("ECS")
request.set_MasterPwd("Lenin1922$")
request.set_DepositType("HALF_MANAGED")
request.set_ZoneId("eu-central-1a")
request.set_SecurityGroupName("emr-security-group")
request.set_ChargeType("PostPaid")
request.set_NetType("vpc")
request.set_VSwitchId("vsw-gw8ue96459069ui8pl8pc")
request.set_VpcId("vpc-gw8b865ld4labpkquw3di")
request.set_AutoRenew(False)
request.set_HighAvailabilityEnable(False)
request.set_ClusterType("HADOOP")
request.set_EmrVer("EMR-3.18.1")
request.set_Name("test-cluster")
request.set_HostGroups([
    {
        "ChargeType": "PostPaid",
        "AutoRenew": False,
        "Period": 1,
        "NodeCount": 2,
        "DiskCount": 1,
        "HostGroupType": "MASTER",
        "HostGroupName": "Master Instance Group",
        "SysDiskCapacity": 120,
        "SysDiskType": "CLOUD_SSD",
        "DiskCapacity": 80,
        "DiskType": "CLOUD_SSD",
        "InstanceType": "ecs.sn1.xlarge",
        "VSwitchId": "vsw-gw8ue96459069ui8pl8pc"
    }
])
request.set_OptionSoftWareLists(["LIVY"])
request.set_UserInfos([
    {
        "UserName": "domdom01",
        "UserId": "12345",
        "Password": "Lenin1922$"
    }
])

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
