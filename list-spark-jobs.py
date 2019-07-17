#!/usr/bin/env python
# coding=utf-8
import os

from aliyunsdkcore.client import AcsClient
from aliyunsdkemr.request.v20160408.ListJobsRequest import ListJobsRequest

client = AcsClient(os.environ['ACCESS_KEY_ID'], os.environ['ACCESS_KEY_SECRET'], 'eu-central-1', timeout=40)

request = ListJobsRequest()
request.set_accept_format('json')

request.set_PageSize(20)
request.set_PageNumber(1)

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
