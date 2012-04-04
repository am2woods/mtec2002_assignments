"""
ascii_times.py
=====
1. create a dictionary of ascii art - {"heart":"<3", "person":">-|o"}
2. loop forever
3. ask for a key
4. ask for the number of times the ascii art should be printed
5. print out the ascii art that number of times
6. what happens if we input a non-numeric value for number of times
7. what happens if we input a key that doesn't exist?
"""
ascii_art = {"heart":"<3","person":">-|o"}

while True:
	print "Which ascii art you want to print"
	user = raw_input('>')
	print "how many times you want to print it"
	num = raw_input('>')
	try:
		print ascii_art[user] * int(num)
	except KeyError:
		print "key does not exists"
	except ValueError:
		print "Not an integer"
		
		
	