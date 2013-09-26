import sys

#open the file
#read it

input_file = sys.argv[1]
f = open(input_file)
file_text = f.read()
f.close()

#create a list to keep the counts in 

letter_counts = [0] * 26

"""
letter_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, 
	"i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, 
	"r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}
"""

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
