# lists :
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# amazon_cart = ['notebook', 'sunglasses']
# print(amazon_cart[0])  # -> notebook
# print(amazon_cart[1])  # -> sunglasses
#
# list slicing :
#
# amazon_cart = ['notebook', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart[0:2])  # -> ['notebook', 'sunglasses']
# print(amazon_cart[0::2])  # -> ['notebook', 'toys']
# amazon_cart[0] = 'laptop'
# print(amazon_cart[0:3])
# print(amazon_cart)  # -> ['laptop', 'sunglasses', 'toys', 'grapes']
#
# matrix:
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0])  # -> [1, 2, 3]
# print(matrix[0][2])  # -> 3
#
# list methods :
#
# basket = [1, 2, 3, 4, 5]
#
# adding :
#
# new_list = basket.append(6)  # ->  The append() method adds a single item to the end of the list.
# new_list2 = basket.insert(3, 3.5)  # -> [1, 2, 3, 3.5, 4, 5, 6]
# basket.extend([7, 8, 9, 10])  # -> [1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]
#
# print(basket)
#
# removing :
#
# basket.pop()  # -> The pop() method removes the item at the given index from the list and returns the removed item.(Clear the end of the list)
# basket.pop(1)  # -> [1, 3, 4]
# print(basket)
#
# basket.remove(4)  # -> The remove() method takes a single element as an argument and removes it from the list.
# # -> [1, 2, 3, 5]
# print(basket)
#
# new_list = basket.pop(4)  # -> return 5
# print(new_list)
#
# basket.clear()  # -> The clear() method removes all items from the list.
# print(basket)
#
# basket = ['a', 'b', 'c', 'd', 'e']
#        # [ 0,   1,   2 ,  3,   4 ]
# print(basket.index('d'))  # -> 3
# print(basket.index('d', 0, 4))  # -> 3
# ( element, start, end)
# The list index() method can take a maximum of three arguments:
#
# element - the element to be searched
# start (optional) - start searching from this index
# end (optional) - search the element up to this index
#
# print('b' in basket)  # -> True
# print('x' in basket)  # -> False
#
# basket = ['a', 'b', 'c', 'c', 'd', 'x', 'e', 'd', 'c']
# basket2 = [1, 5, 6, 10, 2]
# print(basket.count('d'))  # -> 2 # The count() method returns the number of times the specified element appears in the list.
# basket2.sort()  # -> The sort() method sorts the elements of a given list.
# print(basket2)  # -> ['a', 'b', 'c', 'c', 'd', 'd', 'e', 'x']
#
# print(sorted(basket))  # -> ['a', 'b', 'c', 'c', 'd', 'd', 'e', 'x']
#
# new_list = basket.copy()  # -> The copy() method returns a shallow copy of the list.
# print(new_list)
#
# basket.reverse()  # -> The reverse() method reverses the elements of the list.
# print(basket)
#
# common list patterns :
#
# basket = ['a', 'b', 'c', 'c', 'd', 'x', 'e', 'd', 'c']
# print(basket[::-1])  # -> reverse ['c', 'd', 'e', 'x', 'd', 'c', 'c', 'b', 'a']
# print(basket)
#
# print(list(range(1, 100)))  # -> The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.
# sentence = ' '
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'peyman'])
# print(new_sentence)  # -> The join() string method returns a string by joining all the elements of an iterable, separated by a string separator.
#
# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'peyman'])
# print(new_sentence)  # -> hi my name is peyman
#
# list unpacking :
#
# a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)   # -> 1 2 3
#
# a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(other)  # -> [4, 5, 6, 7, 8, 9]
#
#
# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(d)  # -> 9
#
# None :
# new = None
# print(type(new))  # -> <class 'NoneType'>






