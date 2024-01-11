# Python script to dedupe email addresses in a list
# The text file's list of emails must end with an empty line (just a new line char)

inputfile = open('list.txt', 'r') # The input file (sorry about hardcoded filename)
outputfile = open('output.txt', 'w') # The output file

outputlist = []
removedupe = False

for line in inputfile.readlines(): # load input list
    # Check the output file being constructed to find out if
    # the email address is already there; if it is, do not add it.
    for outputlistitem in outputlist:
        if outputlistitem == line:
            # The email address is already in the output file, so
            # do not add it and break out of the inner for loop
            removedupe = True
            break # Breaks out of inner for loop
    if removedupe:
        # Reset removedupe signal
        removedupe = False
    else:
        # Add the email address to the output list
        outputlist.append(line)

# Send the de-duped list of emails to the output text file
for outputline in outputlist:
    outputfile.write(outputline)

# File handling housekeeping
inputfile.close()
outputfile.close()