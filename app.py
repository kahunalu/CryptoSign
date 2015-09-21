import rsa

def validate():
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
		rsa.verify(date, signature, public_key)
		execute()
	except:
		print "License file not valid. Cyber police notified."

def execute():
	print "Program has executed"

validate()
