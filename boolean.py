#boolean
# In programming you often need
# to know if an expression is
# True or False.
print(bool(0))  # -> False
print(bool(1))  # -> True


birth_year = int(input('what year were you born?'))
age = 2020 - birth_year
print(f'you age is : {age}')


# developer fundamentals :
# While it’s good to
# know how to write comments
# in Python, it’s just as vital
# to make sure that your comments
# are readable and easy to understand.


# exercise password checker :

password = input('enter your password : ')
username = input('enter your username : ')
len_pass = len(password)
star_pass = (len_pass * '*')

print(f'{username}, your password {star_pass} is {len_pass} letters long')


