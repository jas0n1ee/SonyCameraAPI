#!/usr/bin/env python
from sonyAPI2 import API2
import cv2
import urllib2
import numpy as np
import time
import struct
api = API2()

api.update_api_list()

try:
    result = api.do('getAvailableCameraFunction')
    current = result['result'][0]
    availavle = result['result'][1]
    if current != "Remote Shooting":
        if "Remote Shooting" in availavle:
            api.do('setCameraFunction',["Remote Shooting"])
            api.update_api_list()
        else:
            print "Remote Shooting not availavle"
except KeyError:
    print result

try:
    result = api.do('getAvailableShootMode')
    current = result['result'][0]
    availavle = result['result'][1]
    if current != "still":
        if "still" in availavle:
            api.do('setShootMode',["still"])
            api.update_api_list()
        else:
            print "stil Shooting not availavle"
except KeyError:
    print result

try:
    result = api.do('actTakePicture')
    url = result['result'][0][0]
except KeyError:
    print result
except TypeError:
    print result
f = urllib2.urlopen(url)
d = np.asarray(bytearray(f.read()), dtype='uint8')
img = cv2.imdecode(d,cv2.IMREAD_COLOR)
cv2.imshow('postview',img)
time.sleep(10)
