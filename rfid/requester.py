import requests
data={"id":10}
x = requests.get('http://localhost:3000',params=data)
print(x.status_code)