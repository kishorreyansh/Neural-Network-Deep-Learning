# Write a python program to find the wordcount in a file (input.txt) for each line and then print the output.
# o Finally store the output in output.txt file

inputfile = open("input.txt", 'r')
outputfile = open("output.txt", 'w')
# We are creating empty dictonary, it stores values in key value pair and it has unique key
d = dict()

# Writing input file content into output file
outputfile.write(inputfile.read() + '\n')
outputfile.write("Word_Count:")
# Reset the file pointer to the beginning of the file
inputfile.seek(0)

for line in inputfile:
    # Remove the leading spaces and newline character
    line = line.strip()
    # we are spliting the line into list of words
    words = line.split()
    for word in words:
        words = word.lower()
        if words in d:
            d[words] = d[words] + 1
        else:
            d[words] = 1
# Write word counts to the output file
for key in list(d.keys()):
    outputfile.write(f"\n{key}: {d[key]}")

# we are closing the input and output files
inputfile.close()
outputfile.close()