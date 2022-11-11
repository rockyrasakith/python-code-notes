# Tried to manually create a list...
myList = []

for i in range(1, 4):
    myList.append(i + 1)
    # print(i + 1)

print("myList: ", myList)
print("Length of myList: ", len(myList))


# The block above can actually create a list without first intializing a variable by 
# using the list method
my_better_list = list(range(4))
print("My better list:", my_better_list)
print("My better list length:", len(my_better_list))


# Ranges using for-loop
for i in range(4):
    print(i)

# Same function as code block above
for i in [0, 1, 2, 3]:
    print(i)

# Creating a list within a range that counts from 0 to 100, but counts up by 2.
# Use the list method and pass in the range method as the argument inside the list method.
# The range method can take three parameters. 
    # The first argument is the begining number of the range.
    # The second number is the ending number of the range.
    # The third argument is the steps that is incremented.

print("This is my list from 1 to 100, counting by 2! ", list(range(0, 100, 2)))

# Loop code that loops the length of the list and also the index of the list:
supplies = ["pens", "staplers", "flame throwers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supples is " + supplies[i])

# Python Multiple Assignments from lists. It's kind of like javascript destructuring?
cat = ["fat", "orange", "loud"]
print("cat_list: ", cat)
size, color, disposition = cat
print("size: ", size)

# Multiple assignments of varibles in one line.
size, description, color = "small", "smart", "black"
print(size, description, color)

# Swapping values from different varibles using the multiple assignment trick
a = "AAA"
b = "BBB"

a, b = b, a
print(a, b)