from itsdangerous import URLSafeSerializer
import rsa
import jwt
from urlobject import URLObject
from passlib.hash import pbkdf2_sha256
from mako.template import Template
import httplib2
from uritemplate import URITemplate
import requests
import chardet
import blinker
from pyasn1.type import univ
#itsdangerous is safely way to pass data to untrusted environments and back.
auth_s = URLSafeSerializer("secret key", "auth")
token = auth_s.dumps({"id": 1, "name": "Mussa"})

print(token)
data = auth_s.loads(token)
print(data["name"])
#rsa is the most widespread and used public key algorithm
publicKey, privateKey = rsa.newkeys(512)
message = "hello brothers and sisters"
encMessage = rsa.encrypt(message.encode(),publicKey)
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("decrypted string: ", decMessage)
#pyjwt is a Python library which allows you to encode and decode JSON Web Tokens

payload_data = {
    "id": "1",
    "name": "Mussa Niyodusenga",
    "nickname": "Moise"
}
my_secret = 'my_secret'
token = jwt.encode(
    payload=payload_data,
    key=my_secret
)
print("token created: ",token)
print(jwt.decode(token, key='my_secret'))
#urlobject is a utility class for manipulating URLs.
url = URLObject("https://github.com/mussa1996/urlobject?spam=tests#mussa")
print(url)
print(url.scheme)
print(url.netloc)
print(url.hostname)
print(url.port)
print(url.path)
print(url.query)
print(url.fragment)

#passlib  is a password hashing library

hash = pbkdf2_sha256.hash("mussa")
print("password hashed: ",hash)
 # verifying the password
verif=pbkdf2_sha256.verify("mussa", hash)
print("password are matched: ",verif)
verif=pbkdf2_sha256.verify("Dan", hash)
print("password not matched: ",verif)

#Mako is a template engine built in Python that is used to generate output HTML, XML and similar formats

tmp = Template("hello ${name}")
print(tmp.render(name="world!"))
mytemplate = Template("hello, ${name}!")
print(mytemplate.render(name="jack"))
#httplib2 provides methods for accessing Web resources via HTTP
#it supports many features, such as HTTP and HTTPS, authentication, caching, redirects, and compression
http = httplib2.Http()
content = http.request("http://www.something.com")[1]
print(content.decode())

#check response status
resp = http.request("http://www.something.com")[0]
print(resp.status)
 
resp = http.request("http://www.something.com/news/")[0]
print(resp.status)
#uritemplate python library to deal with URI Templates
#requests allows you to send HTTP requests using Python

test = URITemplate('https://w3schools.com/python/demopage.htm{/gist_id}')
uri = test.expand(gist_id='123456')
print(uri)
resp = requests.get(uri)
print(resp.text)

#chardet is The Universal Character Encoding Detector

name = b"\x4d\x75\x73\x73\x61"
detection = chardet.detect(name)
print(detection)
encoding = detection["encoding"]
print(name.decode(encoding))
#Blinker provides fast & simple object-to-object and broadcast signaling for Python objects


frobnicated = blinker.signal('frobnicated')
class Receiver(object):
    
    def __init__(self):
        def handle_frobnicated(sender, **kwargs):
            self.on_frobnicated(sender, **kwargs)
        self.handle_frobnicated = handle_frobnicated
        frobnicated.connect(handle_frobnicated)
    def on_frobnicated(self, sender, **kwargs):
        print (sender,kwargs['message'])
       
if __name__ == '__main__':
         receiver = Receiver()
for i in range(10):
    result= frobnicated.send('Sender %s' % i, message='Good morning my people')
print(result)
#pyasn1  is a free and open source implementation of ASN
asn1IntegerValue = univ.Integer(10)
print(asn1IntegerValue - 5)
print(univ.OctetString(b'mussa') == b'mussa')

