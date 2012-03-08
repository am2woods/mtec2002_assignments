"""
equal_to_three_while.py
===
1. Create a list of strings called animals...  "dog", "zebra", "giraffe", "elephant", "cat", "lion", "bear"
2. Create an empty list called three_letter_words
3. Use a while loop to append all of the three letter words from animals to three_letter_words 
4. Print out the animals list and the three_letter_words list

Example Output:
All words: ['dog', 'zebra', 'giraffe', 'elephant', 'cat', 'lion', 'bear']
Three letter words: ['dog', 'cat']
"""
animals = ['dog', 'zebra', 'giraffe', 'elephant', 'cat', 'lion', 'bear']

three_letter_words = []

x = 0

while x < len(animals):
	if len(animals[x]) == 3:
		three_letter_words.append(animals[x])
	x += 1
	
print "All words: %s and three letter words: %s" %(animals, three_letter_words)
	