#!/usr/bin/env python
from sonyAPI2 import API2
import cv2
import urllib2
import numpy as np
import time
import struct
api = API2()

# api.update_url()

api.update_api_list()

try:
    result = api.do('startLiveview')
    url = result['result'][0]
except KeyError:
    print result
f = urllib2.urlopen(url)

#method 1
buff = ''
chunk_size = 8192
for i in xrange(300):
    if len(buff) < chunk_size:
        time_s = time.time()
        buff = buff + f.read(chunk_size)
        # print "Download Speed %f KB/s"%(chunk_size/1000/(time.time() - time_s))
    time_s = time.time()
    start_code = ''.join(buff).find('$5hy')
    # print "LCS time cost", time.time() - time_s

    if start_code < 0:
        buff = buff[-12:]
        print "skip", len(buff)-12
    elif start_code < 8:
        buff = buff[8:]
        print "skip a header"
    else:
        if start_code > len(buff) - 129:
            buff = buff + f.read(chunk_size)
        start_byte = ord(buff[start_code - 8])
        payload_type = ord(buff[start_code - 7])
        sequence_num, = struct.unpack('>I', buff[start_code - 6:start_code - 4].rjust(4,'\0'))
        time_stamp, = struct.unpack('>I', buff[start_code - 4:start_code].rjust(4,'\0'))
        payload_size, = struct.unpack('>I', buff[start_code+4:start_code+7].rjust(4,'\0'))
        padding_size = ord(buff[start_code+8])
        print "StartByte:%d\t sequenceNum:%d\t timeStamp:%d\t Type:%d\t Payload:%d\t Padding:%d\t"%(
            start_byte,sequence_num,time_stamp,payload_type,payload_size,padding_size)

        buff = buff[start_code+128:]
        if payload_type == 1:
            if payload_size + padding_size > len(buff):
                time_s = time.time()
                download_size = payload_size+padding_size-len(buff)
                buff = buff + f.read(download_size)
                # print "Download Speed %f KB/s"%(download_size/1000/(time.time() - time_s))
            img_data = buff[:payload_size]
            buff = buff[payload_size:]

            time_s = time.time()
            d = np.asarray(bytearray(img_data), dtype='uint8')
            img = cv2.imdecode(d,cv2.IMREAD_COLOR)
            cv2.imshow('postview',img)
            cv2.waitKey(10)
            # print "Decode time cost", time.time() - time_s

#method 2
def checkbyte(f):
    if f.read(4) == '$5hy':
        return
    state = 0
    i = 1
    while 1:
        i+=1
        if state == 0 :
            if f.read(1) == '$':
                state = 1
            else:
                state = 0
        if state == 1 :
            if f.read(1) == '5':
                state = 2
            else:
                state = 0
        if state == 2 :
            if f.read(1) == 'h':
                state = 3
            else:
                state = 0
        if state == 3 :
            if f.read(1) == 'y':
                state = 4
            else:
                state = 0
        if state == 4 :
            print 'skip', i
            return
for i in xrange(300):
    buff = f.read(8)
    start_byte = ord(buff[0])
    payload_type, = struct.unpack('>I',buff[1].rjust(4,'\0'))
    sequence_num, = struct.unpack('>I',buff[2:4].rjust(4,'\0'))
    time_stamp, = struct.unpack('>I',buff[4:8])

    #payload header
    checkbyte(f)
    buff = f.read(124)
    payload_size, = struct.unpack('>I',buff[0:3].rjust(4,'\0'))
    padding_size= ord(buff[3])

    print "StartByte:%d\t sequenceNum:%d\t timeStamp:%d\t Type:%d\t Payload:%d\t Padding:%d\t"%(
            start_byte,sequence_num,time_stamp,payload_type,payload_size,padding_size)
    d = f.read(payload_size)
    if padding_size > 0:
        f.read(padding_size)

    if payload_type == 1:
        # Type = 0x01
        d = np.asarray(bytearray(d), dtype='uint8')
        img = cv2.imdecode(d,cv2.IMREAD_COLOR)
        cv2.imshow('postview',img)
        cv2.waitKey(1)

print api.do('stopLiveview')
