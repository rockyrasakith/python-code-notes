# def div42by(divideBy):
#     return 42/divideBy

# print(div42by(1))
# print(div42by(42))
# print(div42by(2))
# print(div42by(5))
# print(div42by(0))

# Use a try/catch statement to handle errors. Code in line 8 will cause an error.
# Here's the solution


def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.")
        
print(div42by(42))
print(div42by(2))
print(div42by(5))
print(div42by(0))
print(div42by(1))