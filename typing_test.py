""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
	""" Returns a list containing each row of the file as a string using its path """
	file = open(path)
	lines = readlines(file)
	all_lines = [strip(x) for x in lines] 
	return all_lines

def new_sample(path, i):
	""" Return the paragraph in the i-th line of the file using its path """
	return lines_from_file(path)[i]

def analyze(sample_paragraph,typed_string,start_time,end_time):
	""" Returns the Words Per Minute Speed and the Accuracy % of the user's typing """
	def words_pm(sample_paragraph,typed_string,start_time,end_time):
		length = len(typed_string)
		delta_time = end_time - start_time
		new_length = length/5
		wpm = new_length * (60/delta_time)
		return wpm
	def accuracy(sample_paragraph,typed_string):
		acc = 0
		list_para = sample_paragraph.split()	
		list_typed = typed_string.split()
		if len(list_para) < len(list_typed):
			list_typed = list_typed[:len(list_para)]
		for k in range(len(list_typed)):
			if list_typed[k] == list_para[k]:
				acc += 1
		if acc == 0:
			acc_percent = 0.0
		else:
			acc_percent = (acc/len(list_typed))*100
		return acc_percent
	wpm = words_pm(sample_paragraph,typed_string,start_time,end_time)
	acc = accuracy(sample_paragraph,typed_string)
	return [wpm,acc]



def pig_latin(str):
	""" Translates a given string to Pig Latin """
	value_index = 0
	arr_str = list(str)
	list_vowels = ['a', 'e', 'i', 'o', 'u'] 
	if str[0] in list_vowels:
		return str + 'way'
	for k in range(len(str)):
		if arr_str[k] in list_vowels:
			value_index = k
			break
	return str[value_index:] + str[:value_index] + 'ay'

def autocorrect(user_input,words_list,score_function):
	""" Autocorrects the input word using the words_list and the custom score_function """
	if user_input in words_list:
		return user_input
	close_word = ''
	score_low = 100
	for word in words_list:
		word_score = score_function(user_input, word)
		if score_low > word_score:
			score_low, close_word = word_score, word
	return close_word


def swap_score(str1, str2):
	""" Returns the number of characters needed to substitute to change the characters 
	in the first string into the corresponding characters in the second string. """
	if str1 == "" or str2 == "":
		return 0
	elif str1[0] == str2[0]:
		return swap_score(str1[1:], str2[1:])
	else:
		return 1 + swap_score(str1[1:],str2[1:])

# END Q1-5

# Question 6
def score_function(str1,str2):
    len1,len2 = len(str1),len(str2)
    if len1 == 0: 
        return len2 
    if len2 == 0: 
        return len1 
    if str1[len1-1]==str2[len2-1]: 
        return score_function(str1[:-1],str2[:-1])    
    add_char = score_function(str1,str2[:-1])
    remove_char = score_function(str1[:-1],str2)
    substitute_char = score_function(str1[:-1],str2[:-1])
    return 1 + min(add_char,remove_char,substitute_char) 

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
def score_function_accurate(str1,str2):
    len1,len2 = len(str1),len(str2)
    if len1 == 0: 
        return len2 
    if len2 == 0: 
        return len1 
    if str1[len1-1]==str2[len2-1]: 
        return score_function_accurate(str1[:-1],str2[:-1])    
    add_char = score_function_accurate(str1,str2[:-1])
    remove_char = score_function_accurate(str1[:-1],str2)
    substitute_char = score_function_accurate(str1[:-1],str2[:-1])+KEY_DISTANCES[str1[len1-1],str2[len2-1]] - 1 
    return 1 + min(add_char,remove_char,substitute_char) 
	
memo = {}
def score_function_final(str1,str2):
	len1,len2 = len(str1), len(str2)
	if len1 == 0:
		return len2
	elif len2 == 0:
		return len1
	else:
		if (str1,str2) not in memo:
			if str1[0] == str2[0]:
				val = score_function_final(str1[1:], str2[1:])
			else:
				pair_key = (str1[0],str2[0])
				distance = KEY_DISTANCES[pair_key]
				val = min(distance+score_function_final(str1[1:],str2[1:]),
							1 + score_function_final(str1[1:],str2),
							1 + score_function_final(str1,str2[1:]))
			memo[(str1,str2)] = val
		return memo[(str1,str2)]
# END Q7-8 
