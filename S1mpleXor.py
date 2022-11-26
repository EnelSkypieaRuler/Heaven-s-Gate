from Crypto.Util.number import bytes_to_long
from secret import key

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

with open('nextstep.txt','r') as f:
    msg=''.join(f.readlines())

with open('output.txt','w') as p:
    p.write(xor(msg,key))

print("Can you figure out the next step?")