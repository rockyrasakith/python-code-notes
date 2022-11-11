spam = ["hello", "hi", "howdy", "nihao"]

# All lists have a method called index() that will return the index for the value of the argument that's
# passed into the method.
print(spam.index("hello"))

# Don't forget about the append() and insert() methods!
spam.append("hola") #This adds the argument into the end of the list.
print(spam)

# This insert method requires two arguments. 
# The first parameter is the index and the second one is the value that will be inserted
spam.insert(1, "hey") 
print(spam)

# Lists also have a remove method(). The remove method allows you to specify a value to remove.
spam.remove("nihao")
print(spam)

# List of numbers can be sorted easily using the sort() method.
number_list = [4, 5, 9, 3, 1, 2, 7]
number_list.sort()
print(number_list)

# Strings can also be sorted
names_list = ["zack", "bob", "adele", "kathy", "cathy", "randy", "bill"]
names_list.sort()
print(names_list)

# Cool trick! You can reverse the sort by entering an argument of reverse=True
# Other argument is to sort in true alphabetical order is key=str.lower
names_list.sort(reverse=True)
print(names_list)