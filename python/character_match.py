# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	arr1 = list(string1.lower().replace(" ", ""))
	arr2 = list(string2.lower().replace(" ", ""))

	for i, letter in enumerate(arr1):
		if letter in arr2:
			index_of_letter = arr2.index(letter)
			arr2[index_of_letter] = ''
		else:
			return False
	if not "".join(arr2):
		return True


# Part 2
def anagrams_for(word, list_of_words):
	word_arr = list(word.lower().replace(" ", ""))
	answer = []
	# iterate through the word_list
	for single_word in list_of_words:
		if len(single_word) == len(word):
			# make a copy of a single_word
			single_word_copy = list(single_word)
			# iterate though the letters of the word
			for letter in word_arr:
				if letter in single_word_copy:
					letter_idx = single_word_copy.index(letter)
					single_word_copy[letter_idx] = ''
			if not "".join(single_word_copy):
				answer.append(single_word)
	return answer