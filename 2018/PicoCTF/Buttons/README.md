Buttons
=======

Points: 250  
Solves: 2356

Flag: `picoCTF{button_button_whose_got_the_button_25a99f84}`


Description
-----------

There is a website running at http://2018shell2.picoctf.com:18342. Try to see if
you can push their buttons. 


Solution
--------

The only thing we have to do is click on the first button. Then, the server give
us a page with, in a link, the text "Button2". When we click on it, we discover
that our access to the flag is denied because "the form is disabled".

The first button send a POST request, the link send a GET request. When
converting into a POST request, we obtains the flag.
