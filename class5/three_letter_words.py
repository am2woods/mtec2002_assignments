"""
Three Letter Words
=====
* Create a list of strings called words that contains "dog","lizard","cat","hawk","pig", and "ibek" 
* Create an empty list called three_letter_words
* Use a for loop to iterate through your words list...
* If the length of your word is equal to 3, append it to your three_letter_words list
* Print "Words: [your words list]"
* Print "Three letter words: [your three_letter_words list]"

Example Output:
Words: ['dog', 'lizard', 'cat', 'hawk', 'pig', 'ibek']
Three letter words: ['dog', 'cat', 'pig']
"""
words = ["cat", "dog", "lizard", "hawk", "pig", "ibek"]

three_letter_words = [(x) for x in words if len(x) == 3]

"""for c in words:
	if len(c) == 3:
		three_letter_words.append(c)"""
	
print "Words: %s and Three letter words: %s" %(words, three_letter_words)