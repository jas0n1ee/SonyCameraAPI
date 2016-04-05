### 索尼大法好
### Basics

Lots of Sony Cameras support remote control through REST API call.
Althought they documents the API thoroughly, the official SDK only contains iOS and Android sample code.


### Quick Links
- [Supported Cameras](https://developer.sony.com/develop/cameras/)  
- [Sony Camera Remote API beta SDK](https://developer.sony.com/downloads/cameras/sony-camera-remote-api-beta-sdk/)

### Quick start

```python
from sonyAPI2 import API2
import cv2
import urllib2
import numpy as np
import time
api = API2()

# Search Camera and update api url
api.update_url()

# Update Available API List
api.update_api_list()

api.do('setShootMode','still')

try:
	result = api.do('actTakePicture')
	url = result['result'][0][0]
except KeyError:
	print result
f = urllib2.urlopen(url)
d = np.asarray(bytearray(f.read()), dtype='uint8')
img = cv2.imdecode(d,cv2.IMREAD_COLOR)
cv2.imshow('postview',img)
time.sleep(10)
```

### License
Apache License
