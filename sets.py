# sets :

# my_set = {1, 2, 3, 4, 5, 5}
# print(my_set)  # -> {1, 2, 3, 4, 5}

# A set is an unordered collection
# of items. Every set element is unique (no duplicates)
# and must be immutable (cannot be changed).
#
# my_set.add(100)
# my_set.add(2)
# print(my_set)  # -> {1, 2, 3, 4, 5, 100}

# my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))  # -> {1, 2, 3, 4, 5}

# print(my_set[0])  # -> TypeError: 'set' object is not subscriptable

# print(1 in my_set)  # -> True
# print(len(my_set))  # -> 5
# print(list(my_set))  # -> convert to list  [1, 2, 3, 4, 5]
#
# new_set = my_set.copy()
# my_set.clear()
# print(new_set)  # -> {1, 2, 3, 4, 5}
# print(my_set)  # -> set()

# my_set = {1, 2, 3, 4, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10}

# difference :

# print(my_set.difference(your_set))  # -> {1, 2, 3} # Returns a set containing the difference between two or more sets
# print(your_set.difference(my_set))  # -> {6, 7, 8, 9, 10}
# print(my_set.discard(5))  # -> Remove the specified item
# print(my_set)  # -> {1, 2, 3, 4}

# print(my_set.difference_update(your_set))  # -> Removes the items in this set that are also included in another, specified set
# print(my_set)  # -> {1, 2, 3}

# print(my_set.intersection(your_set))  # -> Returns a set, that is the intersection of two other sets # {4, 5}
# print(my_set & your_set)  # -> {4, 5}
# print(your_set.intersection(my_set))  # -> {4, 5}

# print(my_set.isdisjoint(your_set))  # -> False # Returns whether two sets have a intersection or not

# my_set = {1, 2, 3}
# your_set = {4, 5, 6, 7, 8, 9, 10}
#
# print(my_set.isdisjoint(your_set))  # -> True

# print(my_set.union(your_set))  # -> 	Return a set containing the union of sets
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(my_set | your_set)  # -> 	Return a set containing the union of sets
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.issubset(your_set))  # -> 	Returns whether another set contains this set or not
# True
print(my_set.issuperset(your_set))  # -> Returns whether this set contains another set or not
# False
print(your_set.issuperset(my_set))  # -> True

print('pepe')









