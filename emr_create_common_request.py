#!/usr/bin/env python
# coding=utf-8

import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'eu-central-1', timeout=40, max_retry_time=5)

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('emr.eu-central-1.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https')  # https | http
request.set_version('2016-04-08')
request.set_action_name('CreateClusterV2')

request.add_query_param('HostGroup.1.HostGroupType', 'MASTER')
request.add_query_param('HostGroup.1.NodeCount', '1')
request.add_query_param('HostGroup.1.InstanceType', 'ecs.sn2.large')
request.add_query_param('HostGroup.1.DiskType', 'CLOUD_EFFICIENCY')
request.add_query_param('HostGroup.1.DiskCapacity', '80')
request.add_query_param('HostGroup.1.DiskCount', '1')
request.add_query_param('HostGroup.2.HostGroupType', 'CORE')
request.add_query_param('HostGroup.2.NodeCount', '2')
request.add_query_param('HostGroup.2.InstanceType', 'ecs.sn2.large')
request.add_query_param('HostGroup.2.DiskType', 'CLOUD_EFFICIENCY')
request.add_query_param('HostGroup.2.DiskCapacity', '80')
request.add_query_param('HostGroup.2.DiskCount', '4')
request.add_query_param('RegionId', 'eu-central-1')
request.add_query_param('Name', 'test-cluster')
request.add_query_param('ClusterType', 'HADOOP')
request.add_query_param('EmrVer', 'EMR-3.18.1')
request.add_query_param('NetType', 'vpc')
request.add_query_param('VpcId', 'vpc-gw8b865ld4labpkquw3di')
request.add_query_param('KeyPairName', 'alibaba-de')
request.add_query_param('VSwitchId', 'vsw-gw8ue96459069ui8pl8pc')
request.add_query_param('ChargeType', 'PostPaid')
request.add_query_param('SecurityGroupName', 'emr-security-group')
request.add_query_param('ZoneId', 'eu-central-1a')

response = client.do_action(request)
# python2: print(response) 
print(str(response, encoding='utf-8'))
