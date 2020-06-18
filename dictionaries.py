# dictionary :

# dictionary = {
#     'a': 1,
#     'b': 2
# }
#
# print(dictionary['b'])  # -> 2
# print(dictionary)  # -> {'a': 1, 'b': 2}

# dictionary = {
#     'a': [1, 2, 3],
#     'b': 'hello',
#     'c': True
# }
#
# my_list = [
#  {
#     'a': [1, 2, 3],
#     'b': 'hello',
#     'c': True
#  },
#  {
#     'a': [4, 5, 6],
#     'b': 'hello',
#     'c': True
#  }
# ]
#
# print(dictionary['a'][1])  # -> 2
# print(my_list[0]['a'][2])  # -> 3

# dictionary = {
#     123: [1, 2, 3],
#     True: 'hello',
#     [100]: True
# }
# print(dictionary[123])  # -> [1, 2, 3]
# print(dictionary[True])  # -> hello
# print(dictionary[100])  # -> TypeError: unhashable type: 'list'

# dictionary = {
#     '123': [1, 2, 3],
#     '123': 'hello',
#     [100]: True
# }
#
# print(dictionary['123'])  # -> (TypeError) dictionary has to be unique because there can only be one key

# dictionary methods :

# dictionary = {
#     'basket': [1, 2, 3],
#     'greet': 'hello',
#     'c': True
# }
#
# # user2 = dict(key = value)
# user2 = dict(name='peyman')
# print(user2)  # -> {'name': 'peyman'}

# dictionary = {
#     'basket': [1, 2, 3],
#     'greet': 'hello',
#     'age': 20
# }


# print('basket' in dictionary)  # -> True
# print('size' in dictionary)  # -> False
# print('hello' in dictionary.keys())  # -> False
# print('age' in dictionary.keys())  # -> True
# print('hello' in dictionary.values())  # -> True
# print(dictionary.items())  # -> dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])
# print(dictionary.clear())  # -> None
# dictionary.clear()
# print(dictionary)  # -> {}
# dictionary2 = dictionary.copy()
# print(dictionary)   # -> {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
# print(dictionary2)  # -> {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}


# dictionary2 = dictionary.copy()
# dictionary.clear()
# print(dictionary)   # {}
# print(dictionary2)  # -> {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}


# print(dictionary.pop('age'))
# print(dictionary)   # -> The pop() method removes and returns an element from a dictionary having the given key.

# print(dictionary.popitem())  # -> ('age', 20) -> last item
# print(dictionary)  # -> {'basket': [1, 2, 3], 'greet': 'hello'}
#
# print(dictionary.update({'age': 55}))
# print(dictionary)  # -> {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55}



