#!/usr/bin/env python
import urllib2
import json

url = "http://192.168.122.1:8080/sony"

'''
Shoot Mode parameters
"still"		Still image shoot mode
"movie"		Movie shoot mode
"audio"		Audio shoot mode
"intervalstill"		Interval still shoot mode
"looprec"	Loop recording shoot mode
'''
def setShootMode(Mode='still', url = url):
	data = {
		'method': "setShootMode",
		'params': [Mode],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getShootMode(url = url):
	data = {
		'method': "getShootMode",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getSupportedShootMode(url = url):
	data = {
		'method': "getSupportedShootMode",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getAvailableShootMode(url = url):
	data = {
		'method': "getAvailableShootMode",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def actTakePicture(url = url):
	data = {
		'method': "actTakePicture",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def awaitTakePicture(url = url):
	data = {
		'method': "awaitTakePicture",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def startLiveview(url = url):
	data = {
		'method': "startLiveview",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def stopLiveview(url = url):
	data = {
		'method': "stopLiveview",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

'''
Live Size options
"L"		XGA size scale (the size varies depending on the camera models, and some camera models change the liveview quality instead of making the size larger.)
"M"	VGA size scale (the size varies depending on the camera models)
'''
def startLiveviewWithSize(Size = 'L', url = url):
	data = {
		'method': "startLiveviewWithSize",
		'params':[Size],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getLiveviewSize(url = url):
	data = {
		'method': "getLiveviewSize",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getSupportedLiveviewSize(url = url):
	data = {
		'method': "getSupportedLiveviewSize",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getAvailableLiveviewSize(url = url):
	data = {
		'method': "getAvailableLiveviewSize",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

'''
Zoom parameters
"in"	Zoom-in
"out"	Zoom-out

Zoom movement parameters
"start"	Long push
"stop"	stop
"1shot"	Short push
'''
def actZoom(param = ['in','1shot'], url = url):
	data = {
		'method': "actZoom",
		'params':param,
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

'''
Zoom setting parameters
"Optical Zoom Only"		Optical zoom only.
"Smart Zoom Only"		Smart zoom only.
"On:Clear Image Zoom"	On:Clear Image Zoom.
"On:Digital Zoom"		On:Digital Zoom.
"Off:Digital Zoom"		Off:Digital Zoom.
'''
def setZoomSetting(param = [{'zoom':'Optical Zoom Only'}], url = url):
	data = {
		'method': "setZoomSetting",
		'params':param,
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getZoomSetting(url = url):
	data = {
		'method': "getZoomSetting",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getSupportedZoomSetting(url = url):
	data = {
		'method': "getSupportedZoomSetting",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getAvailableZoomSetting(url = url):
	data = {
		'method': "getAvailableZoomSetting",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def actHalfPressShutter(url = url):
	data = {
		'method': "actHalfPressShutter",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def cancelHalfPressShutter(url = url):
	data = {
		'method': "cancelHalfPressShutter",
		'params':[],
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def setTouchAFPosition(param = [50,50], url = url):
	data = {
		'method': "setTouchAFPosition",
		'params':param,
		'id':1,
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getTouchAFPosition(url = url):
	data = {
		'id':1,
		'method': "getTouchAFPosition",
		'params': [],
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def cancelTouchAFPosition(url = url):
	data = {
		'id':1,
		'method': "cancelTouchAFPosition",
		'params': [],
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)

def getCameraFunction(url = url):
	data = {
		'id':1,
		'method': "getCameraFunction",
		'params': [],
		'version': "1.0"
	}
	req = urllib2.Request(url + '/camera')
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req, json.dumps(data))
	return json.load(response)