from sets import Set
import sys
print sys.version 

fileName = 'listofUnits.txt'
myFile = open(fileName,'r')
unitDict = set()
for line in myFile:
	if not line:
		continue
	line = line.split()
	line = line[0]
	line = line.lower()
	unitDict.add(line)
	sStr = "s"
	line = line + sStr
	unitDict.add(line)

print("Dictionary built")

if ('tablespoon' in unitDict):
	print("has tablespoon")