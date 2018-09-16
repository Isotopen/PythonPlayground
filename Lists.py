# lists [,]
# strings "" or ''

languages = ["Python", "Javascript", "Java", "C#", "Ruby", "Swift"]
print(languages)
len(languages)
bool(languages)
banner = list("Congratulations")
print(banner)



temperatures = []
temperatures.append(98.6)
temperatures.append(99.4)
temperatures
er_temps = [102.2, 103.5, 101.1, 99.9]
temperatures.extend(er_temps)
primary_care_doctors = ["Dr. Scholls", "Dr. Pepper"]
er_doctors = ["Doug", "Susan"]
all_doctors = primary_care_doctors + er_doctors
all_doctors
primary_care_doctors
temperatures.append(99)
temperatures.append("Burning up")



favorite_things = ["raindrops on roses", "whiskers on kittens", "bright copper kettles"]
favorite_things += ["warm woolen mittens"]
favorite_things.append(["bright paper packages tied with string"])
del favorite_things[-1]
favorite_things.append("bright paper packages tied with string")
favorite_things.extend(["cream colored ponies", "crisp apple strudels"])
del favorite_things[1]
favorite_things.insert(1, "whiskers on kittens")


a = [1, 2, 3]
a.extend("abc")




#Challenge Task 1 of 2
#Alright, my list is messy! Help me clean it up!
#First, start by moving the 1 from index 3 to index 0. Try to do this in a single step by using both .pop() and .insert(). It's OK if it takes you more than one step, though!
messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
messy_list.insert(0, messy_list.pop(3))

#Challenge Task 2 of 2
#Great! Now use .remove() and/or del to remove the string, the boolean, and the list from inside of messy_list. When you're done, messy_list should have only integers in it.
messy_list.remove(messy_list[1])
messy_list.remove(messy_list[3])
messy_list.remove(messy_list[3])

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




numbers = list(range(20))
numbers
