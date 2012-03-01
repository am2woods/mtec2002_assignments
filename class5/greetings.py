"""
greetings.py
=====
Write the following program:
1. Create a list of names and assign to a variable called names
2. Append another name to this list using append
3. Print out the length of this list
4. Loop through each item of this list and print out the name with a greeting, like "hello", appended before it

For example...

Hello Dave
Hello Sue
Hello James
"""

names = ['Ken', 'Ryu', 'Ehonda', 'Chun-li']

names.append('Cammy')

print len(names)

for c in names:
	print "Hello %s" %(c)

