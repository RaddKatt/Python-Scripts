# Retreives SAP tcode descriptions from a lookup site

import urllib.request
import re

tcodesFound = 0
tcodesNotFound = 0

print('\n')

sourceFile = open('SAP-Transaction-Codes-test1.txt','r')
for tcode in sourceFile.readlines():
    tcode = re.sub('\n','', tcode.rstrip())
    try:
        req = urllib.request.Request('http://www.tcodesearch.com/sap-tcodes/detail?id=' + tcode)
        resp = urllib.request.urlopen(req)
        html = resp.read()
        text = html.decode() #Convert the bytes to a string.

        tcodeDesc = re.findall('Description :.*\n.*', text)
        tcodeDesc = str(tcodeDesc[0])
        tcodeDesc = re.findall('<small>\s+(.*)</small>', tcodeDesc)
        tcodeDesc = str(tcodeDesc[0])
        tcodeDesc = re.sub('\s*$','', tcodeDesc.rstrip())
        print(tcode + ',Not_Found,' + tcodeDesc)
        tcodesFound += 1

    except:
        tcodesNotFound += 1
        continue

print('\nDone.')
print('Tcodes Found: ' + str(tcodesFound))
print('Not Found: ' + str(tcodesNotFound))
