# The following lines assing values to each variable 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

# The following lines print the each respective string along with the current value assigned to the variables
print "There are", cars, "cars available."
print "there are only", drivers "drivers available."
print "there will be", cars_not_driven, "empty cars today"
print 'we can transport', carpool_capacity, "people today."
print 'we have', passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car"