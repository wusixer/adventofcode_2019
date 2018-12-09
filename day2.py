
with open('day2.txt','r') as day2:
	day2_txt=day2.readlines()


# part 1:What is the checksum for your list of box IDs?
# count the number of twos and threes and multiply them together
two=0
three=0
for i in range(len(day2_txt)):
	row=day2_txt[i].strip()
	dict={}
	for j in row:
		if j in dict:
			dict[j]+=1
		else:
			dict[j]=1
	if 2 in dict.values():
		two+=1
	if 3 in dict.values():
		three+=1


print(two, three, two*three)


# part 2: What letters are common between the two correct box IDs?
# use dictionary, compare each word to other words individually, see common ones between 2 boxs
with open('day2.txt','r') as day2:
	day2_list=[line.rstrip('\n') for line in day2]

dict={}
for word1 in range(len(day2_list)):
	for word2 in range(word1+1, len(day2_list)):
		letter=''
		for i in range(26):
			if day2_list[word1][i]==day2_list[word2][i]:
				letter+=day2_list[word2][i]
				print(letter)

		dict[letter]=len(letter)


for key, value in dict.items():
	if value==max(dict.values()):
		print(key)

