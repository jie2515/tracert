#!/usr/bin/python
#_*_coding: utf-8_*_
#version: 0.1
#python2.6 & python3.2
#note

import json
import collections
import sys
import fileinput
import re

reload(sys)
sys.setdefaultencoding('utf-8')

IS_PY_2 = sys.version_info < (3,0)

# 为python2引入urllib2
if IS_PY_2:
	import urllib2
else:
	import urllib.request

def request(url):
	resp = ''
	if IS_PY_2:
		req = urllib2.Request(url)
		req.add_header("apikey", "a385eca47c6735ef0eed7facde78ddbb")
		resp = urllib2.urlopen(req).read().decode("utf-8")
	else:
		req = urllib.request.Request(url)
		req.add_header("apikey", "a385eca47c6735ef0eed7facde78ddbb")
		resp = urllib.request.urlopen(req).read().decode("utf-8")
	return resp

class IPInfo (object):
	head_text = {
		'city': u'城市',
		'ret_code': u'返回码',
		'ip': u'ip',
		'region': u'地区',
		'country': u'国家',
		'county': u'县',
		'isp': u'服务提供商',
	}

	custom_sort = [
		'ip',
		'isp',
		'country',
		'city',
		'region',
		'county',
	]

	def __init__(self, ip_info):
		self._ip_info = ip_info

		for i in self.head_text:
			if not self._ip_info.has_key(i):
				self._ip_info[i] = u""

	def __str__(self):
		text = u''
		for i in self.custom_sort:
			text = text + "%s " % (self._ip_info[i])
		return text





url = "http://apis.baidu.com/showapi_open_bus/ip/ip?ip="
#url = "http://apistore.baidu.com/microservice/iplookup?ip="
#http://apistore.baidu.com/apiworks/servicedetail/2565.html

pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

for line in fileinput.input():
	if line:
		exit()
	else:
		#print('---'+line)
		ip = re.findall(pattern,line)
		#print(ip)
		all_ip = len(ip)
		cur_idx = 1
		for n in ip:
			_url = url + n
			#print(_url)
			#request = urllib.request.urlopen(url).read().decode("utf-8")
			#info = json.loads(result,object_pairs_hook=collections.OrderedDict)
			resp = request(_url)
			#print('resp' '%s' % resp)
			info = json.loads(resp)
			# info = json.loads(resp,object_pairs_hook=collections.OrderedDict)
			if((info)['showapi_res_code'] == -1):
				#print(info)
				print(info['showapi_res_error'])
			else:
				#print('info' '%s' % info)
				#print(type(info))
				#print("%s" % info.get('showapi_res_body', 'none').get('isp'))
				#print(info['showapi_res_body']['isp'])
				#print("%s" % (showapi_res_body['isp'])
				#print(info['showapi_res_body']['ip'],": ", info['showapi_res_body']['isp'], info['showapi_res_body']['country'], info['showapi_res_body']['region'],info['showapi_res_body']['city'],info['showapi_res_body']['county'])
				"""
				print(" %s %s %s %s %s %s " % (
					info['showapi_res_body']['ip'],
					info['showapi_res_body']['isp'],
					#info.get['showapi_res_body']['isp'],
					info['showapi_res_body']['country'],
					info['showapi_res_body']['region'],
					info['showapi_res_body']['city'],
					info['showapi_res_body']['county'])
				)
				"""
				text = IPInfo(info['showapi_res_body'])
				print(text)
	