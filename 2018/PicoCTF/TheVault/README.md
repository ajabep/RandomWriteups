The Vault
=========

Points: 250  
Solves: 1807

Flag: `picoCTF{w3lc0m3_t0_th3_vau1t_c09f30a0}`


Description
-----------

There is a website running at http://2018shell2.picoctf.com:56537. Try to see if
you can login!


Solution
--------

The only thing we have to do is complete a login form. And we have sources. In
this code, we find a SQL injection, and a very basic blacklist filter (`$pattern
="/.*['\"].*OR.*/i";`). It does not filter every kind of SQL injection payloads.
In SQL language, we could use, in others, the keyword `UNION`, to union results
of two SQL requests.

The original request is `SELECT 1 FROM users WHERE name='$username' AND
password='$password'`. If the password is something like `' UNION SELECT 1 FROM
users WHERE 'A'='A`, the final request will be `SELECT 1 FROM users WHERE
name='$username' AND password='' UNION SELECT 1 FROM users WHERE 'A'='A'`, it
will return `1` and the PHP script will understand that we have good
credentials.
