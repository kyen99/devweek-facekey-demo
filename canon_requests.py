import requests
import json
import urllib.request
import urllib

#reset the zoom level to 0

zoom_reset_payload = json.dumps({"value": 0,
"ability": {"min":0, "max":100, "step":1}})

zoom_reset = requests.post(url = 'http://192.168.1.2:8080/ccapi/ver100/shooting/control/zoom',data=zoom_reset_payload)




#zoom in to 50%
zoom_in_payload = json.dumps({"value": 50,
"ability": {"min":0, "max":100, "step":1}})

zoom_in = requests.post(url = 'http://192.168.1.2:8080/ccapi/ver100/shooting/control/zoom',data=zoom_in_payload)

zoom_in


#take the photo
take_payload = json.dumps({'af': True})
take_photo = requests.post(url='http://192.168.1.2:8080/ccapi/ver100/shooting/control/shutterbutton',data = take_payload)

take_photo

#download the photo

r = requests.get("http://192.168.1.2:8080/ccapi/ver100/contents/sd/100CANON")
image = r.json()["url"][-1]

image
imagename = image[-12:]
imagename
#download the image to local folder
urllib.request.urlretrieve(image,imagename)
