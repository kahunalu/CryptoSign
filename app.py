'''
Assignment 1, Seng 360
Luke Mclaren V00763009
'''

import rsa
import time

def validate():
	#Public Key
	public_key = '-----BEGIN RSA PUBLIC KEY-----\nMEgCQQDoTcl289XVSXh1PEgMl4rlXN73ycB3GvEyqb9VXMocsFJ2aBvH9gGTJNxy\nx0WH7hAXhuAfRiS5WQpZ+sUKlXFzAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
	signature = ''

	try:
		f = open('license.txt', 'r')
	except:
		print "License file not found"
		return

	public_key = rsa.PublicKey.load_pkcs1(public_key, format='PEM')

	date = f.readline().rstrip()	

	for line in f:
		signature = signature+line

	try:
		#Verification step
		rsa.verify(date, signature, public_key)
		date = time.strptime(date, "%d/%m/%Y")
		if date > time.localtime():
			execute()
	except:
		print "License file not valid. Cyber police notified."

def execute():
	print "Program has executed"

validate()
