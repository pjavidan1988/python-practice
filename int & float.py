# Numbers :
# int (signed integers) : 10, 2, -10, ...
# print(type(10))
# float (floating point real values) : 0.0, 15.20, -21.9, ...
# print(type(0.0))
# complex (complex numbers) : 3.14j,  45.j, 9.322e-36j, ...
# print(type(3.14j))
#---------- tip
# print(2 ** 3)  # power
# print(80 // 52)  # rounded down integer
# print(6 % 4)  # remainder of this division

# math functions :

# print(round(3.9))  # rounding the number to the side that is closer
# print(abs(-20))  # return the absolute value of the argument(Don't be negative)
# (search google for other math function)


# developer fundamentals :

# don't read the dictionary


# operator precedence :

print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

# optional bin() :

# The bin() method converts and
# returns the binary equivalent
# string of a given integer.
# If the parameter isn't an integer, it has
# to implement __index__() method to return
# an integer.

print(bin(5))
print(int('0b101', 2))

# variables :

#Variables are nothing but reserved memory
# locations to store values.
# It means that when you create a variable,
# you reserve some space in the memory.
# The equal sign (=) is used to assign values to variables.
# The operand to the left of the = operator is the
# name of the variable and the operand to the right
# of the = operator is the value
# stored in the variable.
counter = 100
print(counter)

# snake_case -> user_iq = 190
# start with lowercase or underscore
# letters, numbers, underscore
# case sensitive
# don't overwrite keywords -> print = 190 -> the mistake

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


# Augmented Assignment Operator :

# some_value = 5
# some_value = some_value + 5
#
#
# print(some_value)


# some_value = 5
# some_value += 5
#
#
# print(some_value)


# some_value = 5
# some_value -= 5
#
#
# print(some_value)


# some_value = 5
# some_value *= 5
#
# print(some_value)