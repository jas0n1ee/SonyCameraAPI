#!/usr/bin/env python
import socket
import netifaces
import urllib2
import xml.etree.ElementTree as ET
MCAST_GRP = '239.255.255.250'
MCAST_PORT = 1900

DISCOVERY_MSG = ('M-SEARCH * HTTP/1.1\r\n' +
                 'ST: urn:schemas-sony-com:service:ScalarWebAPI:1\r\n' +
                 'MX: 3\r\n' +
                 'MAN: "ssdp:discover"\r\n' +
                 'HOST: 239.255.255.250:1900\r\n\r\n')

def local_interfaces():
	interfaces = netifaces.interfaces()
	print "Trying interfaces:",interfaces
	for i in interfaces:
		try :
			ip = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']
		except KeyError:
			pass
		else:
			yield ip

def interface_addresses(family=socket.AF_INET):
	for ip in local_interfaces():
		for fam, _, _, _, sockaddr in socket.getaddrinfo(ip, 2333):
			if family == fam:
				yield sockaddr[0]
def get_api_url():
	url = ''
	for addr in interface_addresses():
		if addr.split('.')[0] == '192':
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
			socket.setdefaulttimeout(1)
			sock.bind((addr, 2333))
			sock.sendto(DISCOVERY_MSG, (MCAST_GRP, MCAST_PORT))
			try:
				data = sock.recv(1024)
			except socket.timeout:
				pass
			else:
				for line in "".join(data).split('\n'):
					if line.split(': ')[0] == 'LOCATION':
						url = line.split(': ')[1]
						break
				if len(url) > 5 :
					print 'Find config xml at:' + url
					break
				else:
					return None
	f = urllib2.urlopen(url)
	content = f.read()
	root = ET.fromstring(content)
	namespace = "urn:schemas-upnp-org:device-1-0"
	try:
		device = root.findall('{%s}device'%(namespace))[0]
	except IndexError:
		return None
	namespace = "urn:schemas-sony-com:av"
	try:
		DeviceInfo = device.findall('{%s}X_ScalarWebAPI_DeviceInfo'%(namespace))[0]
	except IndexError:
		return None
	try:
		ServiceList = DeviceInfo.findall('{%s}X_ScalarWebAPI_ServiceList'%(namespace))[0]
	except IndexError:
		return None
	Services = ServiceList.findall('{%s}X_ScalarWebAPI_Service'%(namespace))
	try:
		url = Services[0].findall('{%s}X_ScalarWebAPI_ActionList_URL'%(namespace))[0].text
	except IndexError:
		return None
	print 'Camera API URL:' + url
	return url