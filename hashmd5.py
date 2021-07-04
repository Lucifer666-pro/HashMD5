#The python program String to MD5 hash method
#Ajith R B


import hashlib;
string=input ("Enter the String to MD5 hash:")
result = hashlib.md5(string.encode())
print("The hexadecimal equivalent of hash is : ", result.hexdigest())
