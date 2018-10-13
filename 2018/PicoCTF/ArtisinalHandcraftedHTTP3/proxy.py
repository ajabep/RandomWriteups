#!/usr/bin/env python3

import pwn
import sys

pwn.context.log_level = 'debug'

chars = {
    ' /` _\\  ': (1, 6),
    ' /` .\\  ': (2, 8),
    '__  __  ': (3, 8),
    '   /\\   ': (4, 8),
    ' || /\\  ': (5, 8),
    '  /||\\  ': (6, 8),
    '__ / /  ': (7, 8),
    ' |  |\\  ': (8, 8),
    ' ||\\.\\  ': (9, 8),
    '  | |   ': ('+', 8),
    '  __    ': ('-', 9),
    '  _\\ /  ': ('*', 7),
}

def get_captcha_reply(captcha):
    """probably the wrost way to parse this captcha"""
    def get_char_at(pos, captcha):
        char_chars = [line[pos-1:pos] for line in captcha.split(b'\n')]
        key = ''.join([ str(s, 'ascii') for s in char_chars])
        if key == '   |    ':
            return get_char_at(pos+2, captcha)
        if key == ' |  .\\  ':
            return get_char_at(pos+2, captcha)
        return chars[key]

    pos = 1

    a, size = get_char_at(pos, captcha)
    pos += size
    pwn.log.info("a=%d" % a)

    op, size = get_char_at(pos, captcha)
    pos += size
    pwn.log.info('op=%s' % op)

    b, size = get_char_at(pos, captcha)
    pos += size
    pwn.log.info('b=%d' % b)
    
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '+':
        return a + b
    pwn.log.error("Ops not found (%s)" % op)

while True:
    progress = pwn.log.progress('Openning server')

    progress.status('openning connection')
    remotesock = pwn.remote('2018shell2.picoctf.com', 46083)

    progress.status('recieve captcha')
    remotesock.recvlines(4)  # Remove first lines
    captcha = remotesock.recvuntil('\n> ')
    captcha = captcha[:-len('\n> ')]
    res = get_captcha_reply(captcha)
    pwn.log.info(res)

    progress.status('replying captcha')
    remotesock.send(str(res))

    progress.status('verifing')
    if b'Validation succeeded.  Commence HTTP.' not in remotesock.recvline():
        pwn.log.error("Not the good reply")
    remotesock.clean()

    progress.success('done')

    localsock = pwn.listen(8888)
    _ = localsock.wait_for_connection()
    localsock.connect_both(remotesock)
