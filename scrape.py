import urllib.request
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://adithyacas.edu.in/gallery/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    images = re.findall(r'<img[^>]+src="([^">]+)"', html)
    print("Found images on main gallery:")
    for img in images:
        print(img)
except Exception as e:
    print("Error:", e)
