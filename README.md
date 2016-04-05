### 索尼大法好
### Basics

Lots of Sony Cameras support remote control through REST API call.
Althought they documents the API thoroughly, the official SDK only contains iOS and Android sample code.


### Quick Links
- [Supported Cameras](https://developer.sony.com/develop/cameras/)  
- [Sony Camera Remote API beta SDK](https://developer.sony.com/downloads/cameras/sony-camera-remote-api-beta-sdk/)

### Quick start

```python
from sonyAPI2 import API

api = API()

# Search Camera and update api url
api.update_url()

# Update Available API List
api.update_api_list()

api.do('setShootMode','still')
api.do('actTakePicture')
```

### License
Apache License
