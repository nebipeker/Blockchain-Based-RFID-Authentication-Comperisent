import os
import hashlib
def trigger_query(uid):
    f = open("uid.txt", "w")
    salt = "s"
    
    hashed_string = hashlib.sha256((str(uid)+salt).encode("utf-8")).hexdigest()
    print(hashed_string)
    f.write(hashed_string)
    
    f.close()
    
    a = os.system('cmd /c "brownie run UIDCheck.py"')
    return a
