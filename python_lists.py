# This is a list

first_list = ["hello", "world", "my", "name"]
print(first_list)

response = input("Add something to this list? Start typing... ")

first_list.append(str(response))
print(first_list)

# list of lists
spam = [[1, 2, 3, 4, 5], ["cat", "bat"], [9, "bat"]]
print("spam[0]: ", spam[0])
print("spam[1]: ", spam[1])
print("spam[2]: ", spam[2])
print("spam[2]: should = 9", spam[2][0])

print(first_list[-1])

# slices of lists first_list[1:3] means that it starts at index one and goes up to but
# doesn't include index three.

new_first_list = first_list[1:3]
print(new_first_list)

new_first_list[2:3] = ["cat", "dog", "mouse"]
print(new_first_list)

# delete index 2 from list
del new_first_list[2]
print(new_first_list)
