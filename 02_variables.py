# Declare and print some variables to test the data types
firstName = 'John'
lastName = 'Doe'
fullName = firstName + ' ' + lastName
country = 'US'
city = 'Miami'
age = 48
year = 2020
is_married, is_true, is_light_on = False, True, True

# Print the data types
# to concatenate is required to use str(), in addition to concatenate different types
print(firstName + ' is a ' + str(type(firstName)))
print(lastName + ' is a ' + str(type(lastName)))
print(fullName + ' is a ' + str(type(fullName)))
print(country + ' is a ' + str(type(country)))
print(city + ' is a ' + str(type(city)))
print(str(age) + ' is a ' + str(type(age)))
print(str(year) + ' is a ' + str(type(year)))
print(str(is_married) + ' is married? ' + str(type(is_married)))
print(str(is_true) + ' is true? ' + str(type(is_true)))
print(str(is_light_on) + ' is light on ' + str(type(is_light_on)))

# Testing some python functions
print('len(' + firstName + ') is ' + str(len(firstName)))
print('len(' + lastName + ') is ' + str(len(lastName)))
print('len(' + fullName + ') is ' + str(len(fullName)))