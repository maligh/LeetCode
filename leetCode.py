#!/usr/bin/python3
# -*- coding: utf-8 -*

import json
import urllib.request
import ssl

def getJson(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	request = urllib.request.Request(url=url, headers=headers)
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen(request,context=context)
	return response.read()
def getProblemArray(jsonString):
	data = json.loads(jsonString)
	array = list(data['stat_status_pairs'])
	array.reverse()
	return array
def getProblemString(array):
	difficultys = ('Easy', 'Middle', 'Hard')
	string = ''
	for x in array:
		string += '| %d |' % x['stat']['frontend_question_id'];
		string += '[%s](https://leetcode.com/problems/%s)' % (x['stat']['question__title'], x['stat']['question__title_slug'])
		string += '|  | %s |  |  |' % difficultys[x['difficulty']['level']-1]
		string += '\n'
	return string

url = 'https://leetcode.com/api/problems/all/'
jsonString = getJson(url)
array = getProblemArray(jsonString)
string = getProblemString(array)
file = open('text.txt', 'w') 
file.write(string)
file.close()
