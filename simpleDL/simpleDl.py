import sys, urllib.request, re

args = len(sys.argv)

if args != 2:
	print('-- Usage: python simpleDl.py <list_file>')

else:
	successes = 0
	failures = 0
	filename = str(sys.argv[1])

	input_file = open(filename, 'r')
	for line in input_file:
		try:
			line = re.sub('\n', '', line)
			url = line
			resource = url.rsplit('/',1)[1]
			print('Downloading ' + resource + '...')
			urllib.request.urlretrieve(url, resource)
			print('\tDone.')
			successes += 1
		except:
			print('\t! Unable to download !')
			failures += 1
	print('Complete. ' + str(successes) + ' successes, ' + str(failures) + ' failures.')