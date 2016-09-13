# Practice project to define a function to build a string
# of all items in a list, using commas and 'and' before the last word
# Written in Python 3.5.1 on Mac

def getItems(listValue):
    myItems1 = ['bike','phone','watch','sunglasses']
    myItems2 = ''
    if listValue in myItems1:
        myItems1[len(myItems1) - 1] =  'and' + ' ' + myItems1[len(myItems1) - 1]
        for item in myItems1:
            myItems2 += item + ', '
        myItems2 = '\'' + myItems2[0:-2] + '\''
        return myItems2

print(getItems('bike'))
