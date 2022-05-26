from brownie import accounts , UIDCheck
import sys

 

def main():
    f= open("uid.txt", "r")
    uid = f.read()
    f.close()
    account = accounts[0]
    f = UIDCheck.deploy({"from":account})
    a = f.checkUid(uid)
    #b = f.checkUid(13514435217237)