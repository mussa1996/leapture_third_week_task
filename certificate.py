#urllib3 is a powerful, user-friendly HTTP client for Python
import certifi
import urllib3
print(certifi.where())
http = urllib3.PoolManager()
req = http.request('GET', 'https://capstone-personal-portofolio.herokuapp.com/api/v2/articles/listAll')
print(req.status)
print(req.data)
