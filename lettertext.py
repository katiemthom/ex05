import sys

#open the file
#read it

f = open(sys.argv[1])
file_text = f.read()
f.close()

#create a list to keep the counts in 

letter_counts = [0] * 26

#iterate through it one letter at a time
# a = 0, b = 1, etc... to z = 25 
#convert each letter to lowercase

for char in file_text: 
	char = char.lower()
	if ord(char) >= 97 and ord(char) <= 122:
		letter_counts[ord(char) - 97] += 1

#when done print list with one entry on each line

for count in letter_counts: 
	print count 
