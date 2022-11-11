# Lists in python can't be copied 
# Importing the copy module to deep copy a list...

import copy

spam = ["duck", "duck", "goose"]

cheese = spam
cheese.append("cat")

# Logically, I would assume the spam list remains the same, and the cheese list is changed.
# However, that's not the case! spam and cheese both get appended!
print(spam)
print(cheese)

# To fix that use the copy.deepcopy() method!

eggs = ["scrambled", "fried", "boiled"]
ham = copy.deepcopy(eggs)
ham.append("baked")
print(eggs)
print(ham)

# Voila! Ham is it's own list!