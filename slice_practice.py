# lists [,]
# dictionaries {:}
# strings "" or ''
# tuple (,) or tuple([1, 2, 3])


#Challenge Task 1 of 3
#Let's get in some slice practice!
#Create a new variable named slice1 that has the second, third, and fourth items from favorite_things.
favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
slice1 = favorite_things[1:4]
#Challenge Task 2 of 3
#Great work! OK, let's do another test. Get the last two items from favorite_things and put them into slice2.
slice2 = favorite_things[5:]
#Challenge Task 3 of 3
#Alright, let's make this last step a bit harder and do two things.
#Make a copy of favorite_things and name it sorted_things.
#Then use .sort() to sort sorted_things.
sorted_things = favorite_things.copy()
sorted_things.sort()
print(favorite_things)
print(slice1)
print(slice2)
print(sorted_things)
