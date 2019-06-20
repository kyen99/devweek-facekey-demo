import requests
r = requests.get("http://192.168.1.2:8080/ccapi/ver100/contents/sd/100CANON")
r.json()["url"][-1]


from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
i

from simple_websocket_server import WebSocketServer, WebSocket


import sys
import yubico
from yubico_client import Yubico

try:
    yubikey = yubico.find_yubikey(debug=False)
    print( "Version : %s " % yubikey.version())
except yubico.yubico_exception.YubicoError as e:
    print( "ERROR: %s" % e.reason)
    sys.exit(1)




client = Yubico('client id', 'secret key')
client.verify('otp')
