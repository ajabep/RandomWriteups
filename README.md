Random Writeups
===============

Where I publish some of my writeups.

TOC
---

### CTF Writeups

* [DefCamp CTF 2018](2018/D-CTF/)
* [PicoCTF 2018](2018/PicoCTF/)


### Type of vulns

#### Crypto

* Bad random -- seed predictable
	* [2018/D-CTF/lucky2/](2018/D-CTF/lucky2/)
* CBC without integrity / IV altering
	* [2018/D-CTF/SecureLogon/](2018/D-CTF/SecureLogon/)
* Padding Oracle
	* [2018/D-CTF/MagicPaddingOracle/](2018/D-CTF/MagicPaddingOracle/)


#### Exploit

* Buffer Overflow -- stack variable writing
	* [2018/D-CTF/lucky/](2018/D-CTF/lucky/) (rewrite a random seed stored on the stack)


#### Web
* Bad captcha -- automatable
	* [2018/PicoCTF/ArtisinalHandcraftedHTTP3/](2018/PicoCTF/ArtisinalHandcraftedHTTP3/)
* Bad HTTP state strorage
	* [2018/PicoCTF/HelpMeReset2/](2018/PicoCTF/HelpMeReset2/) (TL;DR: just replay the cookie until it's OK)
* Command injection
	* [2018/PicoCTF/fancy-alive-monitoring/](2018/PicoCTF/fancy-alive-monitoring/)
* SQL injection
	* [2018/PicoCTF/ASimpleQuestion/](2018/PicoCTF/ASimpleQuestion/) (basic, no tricks)
	* [2018/PicoCTF/TheVault/](2018/PicoCTF/TheVault/) (basic, very very bad filtering)
* Template injection
	* [2018/PicoCTF/Flaskcards/](2018/PicoCTF/Flaskcards/)
	* [2018/PicoCTF/FlaskcardsandFreedom/](2018/PicoCTF/FlaskcardsandFreedom/)
