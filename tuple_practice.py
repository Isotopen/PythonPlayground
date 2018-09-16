# lists [,]
# dictionaries {:}
# strings "" or ''
# tuple (,) or tuple([1, 2, 3])




#def add(*nums):
#    total = 0
#    for num in nums:
#        total += num
#    return total

def add(base, *args):
    total = base
    for num in args:
        total += num
    return 
    
def subtract(base, *args): # this one is unproven
    total = base
    for num in args:
        total -= num
    return total

def multiply(base, *args):
    total = base
    for num in args:
        total *= num
    return total    


for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1, letter))


# Challenge Task 1 of 1
# Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:
# All uppercase
# All lowercase
# Titlecased (first letter of each word is capitalized)
# Reversed
# There are str methods for all but the last one.

def stringcases(string_to_case):
    return (string_to_case.upper(), string_to_case.lower(), string_to_case.title(), string_to_case[::-1])




# Challenge Task 1 of 1
# Alright, this one can be tricky but I'm sure you can do it.
# Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever.
# Your function should return a list of tuples. Each tuple should hold the first item in each iterable, then the second set, then the third, and so on. Assume the iterables will be the same length.
# Check the code below for an example.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(iterable1, iterable2):
    output = []
    for item in range(0, len(iterable1)):
        output += (iterable1[item], iterable2[item]),
    return output


