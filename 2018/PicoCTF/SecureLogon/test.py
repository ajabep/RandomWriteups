#!/usr/bin/env python3

from base64 import b64decode
from base64 import b64encode

BLOCKSIZE = 16  # AES treat always 128bits blokcs (even for AES 192 or 256)
AES_KEY = "SECRET_KEY" # Change it as you wish

pad = lambda s: s + (BLOCKSIZE - len(s) % BLOCKSIZE) * \
            chr(BLOCKSIZE - len(s) % BLOCKSIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def xor(a, b):
    c = b''
    assert len(a) == len(b)
    if isinstance(a, str):
        a = a.encode('utf-8')
    if isinstance(b, str):
        b = b.encode('utf-8')

    for i in range(len(a)):
        c += bytes([ a[i] ^ b[i] ])
    return c

print("Verify xor function")

assert xor(b'\x00', b'\x00') == b'\x00'
assert xor('\x00', '\x00') == b'\x00'
assert xor('\x00', b'\x00') == b'\x00'

assert xor(b'\x00', b'\x05') == b'\x05'
assert xor(b'\xFF', b'\x05') == b'\xFA'

assert xor(b'\x00'*112, b'\x00'*112) == b'\x00'*112
assert xor(b'\xFF'*112, b'\xFF'*112) == b'\x00'*112
assert xor(b'\xFF'*112, b'\x00'*112) == b'\xFF'*112

assert xor(b'\xFF'*112, b'\x00'*80 + b'\xFF'*16 + b'\x00'*16) \
        == (b'\xFF'*80 + b'\x00'*16 + b'\xFF'*16)

print("___________________")


print("Computing mask")

having_clear = '{"admin": 0, "pa'
wanted_clear = '{"admin": 1, "pa'

MASK = xor(having_clear, wanted_clear)

print("Enter your cookie")
cookie = input()

c_raw = b64decode(cookie)
print(c_raw.hex(), len(c_raw))

PADDED_ATK_MASK = MASK + b'\x00'*(len(c_raw)-len(MASK))
c_fake_raw = xor(c_raw, PADDED_ATK_MASK)
print(c_fake_raw.hex(), len(c_fake_raw))
print(("↑ " + '  '*(BLOCKSIZE-1))*7)  # rule of start bit for AES block

c_fake = b64encode(c_fake_raw)
print('c_fake  ', c_fake, len(c_fake))
