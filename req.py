import requests

res=requests.get("www.gndec.ac.in")
if res.status_code==200:
	print("Successfull")
else:
	print("fail")
