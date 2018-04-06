import re
from operator import itemgetter
with open("sym_dis.txt") as f:
	lines = f.readlines()
	listOfWords = []
	for line in lines:
		words = line.split("\t")
		listOfWords.append(words)
	# print(listOfWords)
	listOfWords = sorted(listOfWords, key=itemgetter(1))
	# print(listOfWords)
	prev_disease = listOfWords[0][1]
	f = open("diseaseSym_dataset/" + str(prev_disease) + ".txt", "w")
	for words in listOfWords:
		cur_disease = words[1]
		if prev_disease == cur_disease:
			f.write(str(words[0]) + ", " + str(words[2]) + ", " + str(words[3]))
		else:
			f.close()
			f = open("diseaseSym_dataset/" + str(cur_disease) + ".txt", "w")
			f.write(str(words[0]) + ", " + str(words[2]) + ", " + str(words[3]))
			prev_disease = cur_disease
	f.close()
		