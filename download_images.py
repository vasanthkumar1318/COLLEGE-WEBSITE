import urllib.request
import re
import os
import ssl
from urllib.parse import urljoin

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://adithyacas.edu.in/gallery/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    images = re.findall(r'<img[^>]+src="([^">]+)"', html)
    
    gallery_dir = os.path.join('images', 'gallery')
    os.makedirs(gallery_dir, exist_ok=True)
    
    count = 1
    for img in images:
        if 'facebook' in img or 'Logo' in img:
            continue
            
        img_url = urljoin(url, img)
        ext = img_url.split('.')[-1].split('?')[0]
        if len(ext) > 4:
            ext = 'jpg'
            
        filename = f"acas-gallery-{count}.{ext}"
        filepath = os.path.join(gallery_dir, filename)
        
        try:
            req_img = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(req_img, context=ctx).read()
            with open(filepath, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded {filename} from {img_url}")
            count += 1
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            
except Exception as e:
    print("Error:", e)
