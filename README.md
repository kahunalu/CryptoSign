
## Assignment 1, Luke Mclaren, V00763009

This program shows an example of how a company may use a asymetric crypto system to sign a 
license file so it may not be tampered with client side.

#### Usage and Dependencies

This program is written in python 2.7.6, and depends on the rsa library which can be installed with:
```
  pip install rsa 
```
and can be executed with the command:
```
  python app.py
```
When the program executes sucessfully it will display the message "Program has executed" message.

### Theory and possible Vulnerabilites 

The license contains a date and a signature which has been generated using a private key.
The public key is then used to decrypt the signature and compare the result to the date, 
if they match the signature has been verified and the program may execute.

This current solution is vulnerable to multiple attacks, 2 of which are fairly simple and would require minimal effort.

  1. Swapping the library used for verification to a malicious library that verifys the signature regardless of reality.
  2. Simpler, change the current time of the computer to a date prior to the license expiration date. 
