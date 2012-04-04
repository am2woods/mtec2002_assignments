"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError

d = {"shape":"circle"}

print d["shape"]

try:
	print d["shape"]
	print d["colors"]
except KeyError:
	print "that key doesn't exist"
	
#ValueError (conversion errors)

try:
	print int("this is no t a number")
except ValueError:
	print "this is not a number"

#TypeError 

try:
	print "foo" * "bar"
except TypeError:
	print "you can't multiply strings"

#IndexError
my_list = ["some", "stuff"]
try:
	print my_list[2]
except IndexError:
	print "You exceeded the index of the list"

#ZeroDivisionError

try:
	print 5/0
except ZeroDivisionError:
	print "that key doesn't exist"

#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score

d = {"score":10}
print d['score']
k = "score"
divisor = 2

try:
	print d[k] / divisor
except KeyError:
	print "that key doesn't exist"
except ZeroDivisonError:
	print "that key doesn't exist"

