from paddingoracle import BadPaddingException, PaddingOracle
import pwn
import json

HOST = '2018shell2.picoctf.com'
PORT = 24933
#HOST = '127.0.0.1'
#PORT = 8888


def byte_to_hex(byte_str):
    return ''.join(["%02X" % x for x in byte_str]).strip()

def hex_to_byte(hex_str):
    bytestring = []

    hex_str = ''.join(hex_str.split(" "))

    for i in range(0, len(hex_str), 2):
        bytestring.append(chr(int(hex_str[i:i+2], 16)))

    return ''.join(bytestring)


resp = open('resp', 'w')

class PadBuster(PaddingOracle):
    def __init__(self, cookie, **kwargs):
        super(PadBuster, self).__init__(**kwargs)
        self.wait = kwargs.get('wait', 2.0)
        self.cookie = cookie

    def oracle(self, data, **kwargs):
        somecookie = byte_to_hex(data)
        print(somecookie)

        if somecookie[32:] == "00000000000000000000000000000000":
            if somecookie[:30] == "000000000000000000000000000000":
                if somecookie[30:32] != '24':
                    raise BadPaddingException()
            elif somecookie[:28] == "0000000000000000000000000000":
                if somecookie[28:30] != '6C':
                    raise BadPaddingException()
            elif somecookie[:26] == "00000000000000000000000000":
                if somecookie[26:28] != 'AC':
                    raise BadPaddingException()
            elif somecookie[:24] == "000000000000000000000000":
                if somecookie[24:26] != 'A7':
                    raise BadPaddingException()
            elif somecookie[:22] == "0000000000000000000000":
                if somecookie[22:24] != '6F':
                    raise BadPaddingException()
            elif somecookie[:20] == "00000000000000000000":
                if somecookie[20:22] != '19':
                    raise BadPaddingException()
            elif somecookie[:18] == "000000000000000000":
                if somecookie[18:20] != '78':
                    raise BadPaddingException()
            elif somecookie[:16] == "0000000000000000":
                if somecookie[16:18] != '62':
                    raise BadPaddingException()
            elif somecookie[:14] == "00000000000000":
                if somecookie[14:16] != 'D7':
                    raise BadPaddingException()
            elif somecookie[:12] == "000000000000":
                if somecookie[12:14] != 'D2':
                    raise BadPaddingException()
            elif somecookie[:10] == "0000000000":
                if somecookie[10:12] != '8F':
                    raise BadPaddingException()
            elif somecookie[:8] == "00000000":
                if somecookie[8:10] != '71':
                    raise BadPaddingException()
            elif somecookie[:6] == "000000":
                if somecookie[6:8] != '27':
                    raise BadPaddingException()
            elif somecookie[:4] == "0000":
                if somecookie[4:6] != 'AF':
                    raise BadPaddingException()
            elif somecookie[:2] == "00":
                if somecookie[2:4] != '96':
                    raise BadPaddingException()
            elif somecookie[0:2] != '32':
                raise BadPaddingException()
        elif somecookie[32:] == "5F96AE25728BD7D165701065ACA0612A":
            if somecookie[:30] == "000000000000000000000000000000":
                if somecookie[30:32] != '9B':
                    raise BadPaddingException()
            elif somecookie[:28] == "0000000000000000000000000000":
                if somecookie[28:30] != '3D':
                    raise BadPaddingException()
            elif somecookie[:26] == "00000000000000000000000000":
                if somecookie[26:28] != 'D4':
                    raise BadPaddingException()
            elif somecookie[:24] == "000000000000000000000000":
                if somecookie[24:26] != '76':
                    raise BadPaddingException()
            elif somecookie[:22] == "0000000000000000000000":
                if somecookie[22:24] != '63':
                    raise BadPaddingException()
            elif somecookie[:20] == "00000000000000000000":
                if somecookie[20:22] != '41':
                    raise BadPaddingException()
            elif somecookie[:18] == "000000000000000000":
                if somecookie[18:20] != 'C5':
                    raise BadPaddingException()
            elif somecookie[:16] == "0000000000000000":
                if somecookie[16:18] != '9C':
                    raise BadPaddingException()
            elif somecookie[:14] == "00000000000000":
                if somecookie[14:16] != '0B':
                    raise BadPaddingException()
            elif somecookie[:12] == "000000000000":
                if somecookie[12:14] != '63':
                    raise BadPaddingException()
            elif somecookie[:10] == "0000000000":
                if somecookie[10:12] != 'FD':
                    raise BadPaddingException()
            elif somecookie[:8] == "00000000":
                if somecookie[8:10] != '80':
                    raise BadPaddingException()
            #elif somecookie[:6] == "000000":
            #    if somecookie[6:8] != '':
            #    raise BadPaddingException()
            #elif somecookie[:4] == "0000":
            #    if somecookie[4:6] != '':
            #    raise BadPaddingException()
            #elif somecookie[:2] == "00":
            #    if somecookie[2:4] != '':
            #    raise BadPaddingException()
            #elif somecookie[0:2] != '':
            #    raise BadPaddingException()
        #elif somecookie[32:] == "5F96AE25728BD7D165701065ACA0612A":
            #if somecookie[:30] == "000000000000000000000000000000":
            #    if somecookie[30:32] != '9B':
            #    raise BadPaddingException()
            #elif somecookie[:28] == "0000000000000000000000000000":
            #    if somecookie[28:30] != '':
            #    raise BadPaddingException()
            #elif somecookie[:26] == "00000000000000000000000000":
            #    if somecookie[26:28] != '':
            #    raise BadPaddingException()
            #elif somecookie[:24] == "000000000000000000000000":
            #    if somecookie[24:26] != '':
            #    raise BadPaddingException()
            #elif somecookie[:22] == "0000000000000000000000":
            #    if somecookie[22:24] != '':
            #    raise BadPaddingException()
            #elif somecookie[:20] == "00000000000000000000":
            #    if somecookie[20:22] != '':
            #    raise BadPaddingException()
            #elif somecookie[:18] == "000000000000000000":
            #    if somecookie[18:20] != '':
            #    raise BadPaddingException()
            #elif somecookie[:16] == "0000000000000000":
            #    if somecookie[16:18] != '':
            #    raise BadPaddingException()
            #elif somecookie[:14] == "00000000000000":
            #    if somecookie[14:16] != '':
            #    raise BadPaddingException()
            #elif somecookie[:12] == "000000000000":
            #    if somecookie[12:14] != '':
            #    raise BadPaddingException()
            #elif somecookie[:10] == "0000000000":
            #    if somecookie[10:12] != '':
            #    raise BadPaddingException()
            #elif somecookie[:8] == "00000000":
            #    if somecookie[8:10] != '':
            #    raise BadPaddingException()
            #elif somecookie[:6] == "000000":
            #    if somecookie[6:8] != '':
            #    raise BadPaddingException()
            #elif somecookie[:4] == "0000":
            #    if somecookie[4:6] != '':
            #    raise BadPaddingException()
            #elif somecookie[:2] == "00":
            #    if somecookie[2:4] != '':
            #    raise BadPaddingException()
            #elif somecookie[0:2] != '':
            #    raise BadPaddingException()

        # TODO manage the lack of connection (n-retries when no connection are possibles)
        sock = pwn.remote(HOST, PORT)
        sock.sendafter('What is your cookie?\n', somecookie + '\n')
        buf = sock.recvall()

        resp.write(somecookie)
        resp.write(buf)
        if 'File "/problems/magic-padding-oracle_4_b6a931ed628517746b8ea88c8688f148/pkcs7.py", line 20, in isvalidpad' in buf:
            raise Exception('Exception for this script')
        if 'invalid padding' in buf:
            raise BadPaddingException()
        pwn.log.info('No padding exception raised on %r', somecookie)

def test_response(new_cookie):
    print('Test the new cookie')
    sock = pwn.remote(HOST, PORT)
    sock.sendafter('What is your cookie?\n', new_cookie + '\n')
    buf = sock.recvall()
    if 'The flag is' not in buf:
        print("Bad cookie")
        return False
    print("Good cookie")
    print("Flag is %s" % buf)
    return True

if __name__ == '__main__':
    pwn.context.log_level = 'warning'

    sock = pwn.remote(HOST, PORT)
    sock.recvuntil('Here is a sample cookie: ')
    cookie_original = sock.recvuntil('\n')[:-1]
    pwn.log.debug('The cookie is %s', cookie_original)
    del sock

    encrypted_cookie = hex_to_byte(cookie_original)
    padbuster = PadBuster(cookie_original)

    cookie_clear = bytearray(b'@\x86\xebLu\x93(\x15\x08\x91\xecE: F\xe6{"username": "guest", "expires": "2000-01-07", "is_admin": "false"}\r\r\r\r\r\r\r\r\r\r\r\r\r')
    #cookie_clear = padbuster.decrypt(encrypted_cookie, block_size=16, iv=bytearray(16))
    print(cookie_clear)
    print('Decrypted somecookie: %s => %r' % (cookie_original, cookie_clear))

    new_cookie = {
        "is_admin": "true",
        "username": "toto",
        "expires": "2019-01-01",
    }
    newcookie_data = json.dumps(new_cookie)
    newcookie_enc = bytearray(hex_to_byte('1B774AA1774AE5E445E13BECB20DDE521CD609CA1C0A97FAF0850F36DB2D643689D19209CB98A1D9D611126F73C32CB8A3E4FC00E19F0720AEE2651200A25AB85F96AE25728BD7D165701065ACA0612A00000000000000000000000000000000'))
    #newcookie_enc = padbuster.encrypt(newcookie_data, block_size=16, iv=bytearray(16))
    print(newcookie_enc)
    print('Encrypted newcookie_data: %s => %r' % (newcookie_data, byte_to_hex(newcookie_enc)))
    test_response(byte_to_hex(newcookie_enc))
