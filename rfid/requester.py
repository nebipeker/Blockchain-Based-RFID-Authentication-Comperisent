import requests
import rsa


'''
(public_key, private_key) = rsa.newkeys(512)
with open("edge_pub.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
with open("edge_priv.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
'''

with open("edge_pub.pem","rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

uid = 13514435217237 # real one
#uid = 13514435217232
uid_b = str(uid)
#print(type(uid_b))
cypher_text = rsa.encrypt(uid_b.encode("utf8"), public_key)
cypher_text
data={"uid":str(cypher_text)[2:-1]}

x = requests.post(url = 'http://localhost:3000',data=cypher_text)
response = x.content.decode('UTF-8')
if response=="0":
    print("Authorized")
else:
    print("Unauthorized")


