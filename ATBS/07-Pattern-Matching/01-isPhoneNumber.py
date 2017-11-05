'''
A phone number–finding program.
It works, but it uses a lot of code to do something limited.
Using regular expressions can accomplish this more easily.
We will demonstrate the 're' module in the next exercise.
'''
#!/usr/local/bin/python3

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True	

if __name__ == '__main__':
	print('\'415-555-4242\' is a phone number: ' + str(isPhoneNumber('415-555-4242')))
	print('\'Moshi moshi\' is a phone number: ' + str(isPhoneNumber('Moshi moshi')))

	message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
	for i in range(len(message)):
		chunk = message[i:i+12]
		if isPhoneNumber(chunk):
			print('Phone number found: %s' % chunk)
	print('Done')
