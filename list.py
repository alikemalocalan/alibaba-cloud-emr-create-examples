#!/usr/bin/env python
# coding=utf-8
import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408.ListClustersRequest import ListClustersRequest

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'eu-central-1', timeout=40,
                   max_retry_time=5)

request = ListClustersRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
