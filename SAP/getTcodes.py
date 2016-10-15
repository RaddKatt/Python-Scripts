# Retreives SAP tcode descriptions from a lookup site

import urllib.request
import re

tcodesFound = 0
tcodesNotFound = 0

print('\n')

sourceFile = open("SAP-Tcodes-No-Descriptions.csv","r")
for tcode in sourceFile.readlines():
    tcode = re.sub('\n','', tcode.rstrip())
    try:
        req = urllib.request.Request('http://www.tcodesearch.com/sap-tcodes/detail?id=' + tcode)
        resp = urllib.request.urlopen(req)
        html = resp.read()
        text = html.decode() #Convert the bytes to a string.

        dataCrop = re.findall("Description :.*\n.*", text)
        dataCrop = str(dataCrop[0])
        dataCrop = re.findall("<small>\s+(.*)</small>", dataCrop)
        dataCrop = str(dataCrop[0])
        dataCrop = re.sub('\s*$','', dataCrop.rstrip())
        print(tcode + ',Not_Found,' + dataCrop)
        tcodesFound += 1

    except:
        tcodesNotFound += 1
        continue

print('\nDone.')
print('Tcodes Found: ' + str(tcodesFound))
print('Not Found: ' + str(tcodesNotFound))
