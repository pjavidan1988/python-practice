# strings
print(type("hello worlds"))  # print <class 'str'>
username = 'peyman1988'
password = 'pepe1366'

# multi line

long_string = '''
wow
o o
---
'''
print(long_string)  # print -> wow
                    #          o o
                    #          ---

# '' -> add space between first name and last name

first_name = 'peyman'
last_name = 'javidan'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation

# print('hello' + 5)  # -> can only concatenate str (not "int") to str

#type conversion

a = str(100)
b = int(a)
c = type(b)
print(c)  # -> <class 'int'>

# escape sequence

weather = "it\'s \"kind of\" sunny"
print(weather)

# \newline	    Ignored
# \\	        Backslash (\)
# \'	        Single quote (')
# \"	        Double quote (")
# \a	        ASCII Bell (BEL)
# \b	        ASCII Backspace (BS)
# \f	        ASCII Formfeed (FF)
# \n	        ASCII Linefeed (LF)
# \r	        ASCII Carriage Return (CR)
# \t	        ASCII Horizontal Tab (TAB)
# \v	        ASCII Vertical Tab (VT)
# \ooo	        ASCII character with octal value ooo
# \xhh...	    ASCII character with hex value hh...

weather = "\t it\'s \"kind of\" sunny \n \t hope you have a good day!"
print(weather)

# formatted string

name = 'peyman'
age = 32

print('hi ' + name + '. you are ' + str(age) + ' years old ')
print(f'hi {name}. you are {age} years old')  # best
print('hi {}. you are {} years old'.format(name, age))
print('hi {1}. you are {0} years old'.format(name, age))
print('hi {new_name}. you are {age} years old'.format(new_name='sally', age=100))


# string indexes

selfish = 'peyman !'
        #  01234567


#[start : stop : step over]

print(selfish[0])  # -> print p
print(selfish[2])  # -> print y
print(selfish[0:2])  # -> print pe
print(selfish[0:8])  # -> print peyman !
print(selfish[1:])   # -> print eyman !
print(selfish[:5])   # -> print peyma
print(selfish[::1])  # -> print peyman !
print(selfish[-1])   # -> print !
print(selfish[-3])   # -> print n
print(selfish[::-1])  # -> print ! namyep ## very useful notation  ## reverse an order

# immutability & Mutable

# Mutable objects:
# list, dict, set, byte array
# Immutable objects:
# int, float, complex, string,
# tuple, frozen set
# [note: immutable version of set], bytes

# Built-In Functions + Methods :

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp

print(len('peyman'))  # Returns the length of an object

quote = 'to be or not to be'
print(quote.upper())  # Converts a string into upper case
print(quote.capitalize())  # Converts the first character to upper case
print(quote.find('be'))  # Searches the string for a specified value and returns the position of where it was found
print(quote.replace('be', 'me'))  # Returns a string where a specified value is replaced with a specified value










