## count the character frequency in a string 
string = 'google.com'
def char_count(string):
	string_dict = {}
	for i in range(len(string)):
		c=0
		for j in range(len(string)):
			if string[i]==string[j]:
				c+=1
		string_dict[string[i]]	= c

	return (string_dict)	
print(char_count(string))
## if not follows poor replace with good else leave unchanged

string = 'The lyrics is not that poor!'
string2='The lyrics is poor!'

def not_poor_check(string):
	poor_pos=string.find('poor!')
	not_pos=string.find('not')
	string_new=''

	if not_pos < poor_pos and not_pos > 0 and poor_pos > 0 :
		string_new=string[:not_pos]+'Good!'
	else:
		string_new = string
	return string_new	

print(not_poor_check(string))
print(not_poor_check(string2))

##find the word with longest length
def longest_word(li):
	li.sort(key=len)
	print(li)
	return li[-1]

li = ['these','are','the','longest','words']
print(longest_word(li))	