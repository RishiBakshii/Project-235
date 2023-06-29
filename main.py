import requests

valid_urls=[]

for i in range(1,5000):
    url=f'http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}'
    res=requests.get(url)
    if res.status_code==200:
        valid_urls.append(url)

print(valid_urls)