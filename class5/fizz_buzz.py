"""
fizzbuzz.py
===
1.  Print integers 1 to 100, but replace multiples of 3 with "Fizz" and multiples of 5 with "Buzz" and multiples of both with "FizzBuzz"
joe@walsh~/projects/archived/fizzbuzz$ python fizzbuzz.py 
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
.
.
"""

a = range(100)

for c in a:
	if c % 3 == 0 and c % 5 == 0:
		print "fizzbuzz"
	elif c % 5 == 0:
		print "Buzz"
	elif c % 3 == 0:
		print "Fizz"
	else:
		print c