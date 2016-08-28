#_*_coding: utf-8_*_
#version: 0.1
#python3.2
#note

import json
import collections
import sys
import fileinput
import re

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



url = "http://apis.baidu.com/showapi_open_bus/ip/ip?ip="
#url = "http://apistore.baidu.com/microservice/iplookup?ip="

pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

for line in fileinput.input():
	#print('---'+line)
	if line:
		ip = re.findall(pattern,line)
		#print(ip)
		for n in ip:
			_url = url + n
			#print(_url)
			#request = urllib.request.urlopen(url).read().decode("utf-8")
			#info = json.loads(result,object_pairs_hook=collections.OrderedDict)
			resp = request(_url)
			info = json.loads(resp)
			# info = json.loads(resp,object_pairs_hook=collections.OrderedDict)
			if((info)['showapi_res_code'] == -1):
		#print(info)
				print(info['showapi_res_error'])
			else:
		#print(info)
				#print(info['showapi_res_body']['ip'],": ", info['showapi_res_body']['isp'], info['showapi_res_body']['country'], info['showapi_res_body']['region'],info['showapi_res_body']['city'],info['showapi_res_body']['county'])
				print( "%s %s %s %s %s %s"  % (
					info['showapi_res_body']['ip'],
					info['showapi_res_body']['isp'],
					info['showapi_res_body']['country'],
					info['showapi_res_body']['region'],
					info['showapi_res_body']['city'],
					info['showapi_res_body']['county'])
				)
			# exit()	
	else:
		fileinput.close()