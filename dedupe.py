# Python script to dedupe email addresses in a list

datafile = open('list.txt', 'r')
outputfile = open('output.txt', 'w')

'''
for line in datafile.readlines():
    if line == "karina.hammes@turner.com\n":
        outputfile.write(line)
        print("found it")
    #print(line, end='')
'''

'''
outputlist = []
for line in datafile.readlines():
    if line == "karina.hammes@turner.com\n":
        outputlist.append(line)
    #print(line, end='')
print(outputlist)
'''

outputlist = ["karina.hammes@turner.com\n"]
#print(outputlist)
for line in datafile.readlines():
    for listitem in outputlist:
        #print(listitem)
        if listitem == line:
            print("It already exists, do nothing")
        else:
            print("Adding it to output")
            print(line)
            outputlist.append(line)
            break

print('======')
print(outputlist)

for outputline in outputlist:
    outputfile.write(outputline) 

'''
for line1 in datafile.readlines():
    for line2 in outputfile.readlines():
        if line1 == "karina.hammes@turner.com\n":
            outputfile.write(line)
            print("found it")
    #print(line, end='')
'''

datafile.close()
outputfile.close()