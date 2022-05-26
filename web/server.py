from aiohttp import request
from bottle import run, get, post, request
import rsa

##############################
@post('/')
def index():
    with open("edge_priv.pem","rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    cypher = request.body.getvalue()
    plain_text = rsa.decrypt(cypher,private_key)
    uid = plain_text.decode("utf8")
    if uid == "13514435217237":
        return '0'
    else:
        return "1"
  
 
##############################
run(host='localhost', port=3000, debug=True, reloader=True)

