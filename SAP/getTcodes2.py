# Retreives SAP tcode descriptions from a lookup site

import urllib.request, re, html

tcodesFound = 0
tcodesNotFound = 0
tcodeList = ['TC,TC_Description,TC_Main_Category,TC_Sub_Category']

def parseValues(searchString):
    parsed = re.findall(searchString, text)
    parsed = str(parsed[0])
    parsed = re.findall('<small>\s+(.*)</small>', parsed)
    parsed = str(parsed[0])
    parsed = html.unescape(parsed)
    parsed = re.sub('\s*$', '', parsed.rstrip())
    parsed = re.sub(',', ';', parsed.rstrip())
    parsed = re.sub('"', '`', parsed.rstrip())
    parsed = re.sub("'", '`', parsed.rstrip())
    return parsed

sourceFile = open('SAP-Transaction-Codes-before.txt','r')
sourceFileLines = sourceFile.readlines()
sourceFileLines.sort()

for tcode in sourceFileLines:
    tcode = re.sub('\n','', tcode.rstrip())
    try:
        req = urllib.request.Request('http://www.tcodesearch.com/sap-tcodes/detail?id=' + tcode)
        resp = urllib.request.urlopen(req)
        resp_html = resp.read()
        text = resp_html.decode() #Convert the bytes to a string.

        tcodeDesc = parseValues('Description :.*\n.*')
        tcodeMainCat = parseValues('Main Category :.*\n.*')
        tcodeSubCat = parseValues('Sub Category :.*\n.*')

        tcodeList.append(tcode + ',' + tcodeDesc + ',' + tcodeMainCat + ',' + tcodeSubCat)
        print(tcode + ',' + tcodeDesc + ',' + tcodeMainCat + ',' + tcodeSubCat)
        tcodesFound += 1

    except:
        tcodesNotFound += 1
        continue

newFile = open('SAP-Transaction-Codes-New.csv', 'w')

for tcode in tcodeList:
  newFile.write("%s\n" % tcode)

print('\nDone.')
print('Tcodes Found: ' + str(tcodesFound))
print('Not Found: ' + str(tcodesNotFound))
