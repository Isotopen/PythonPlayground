#Challenge Task 1 of 5
#This challenge has several steps so take your time, read the instructions carefully, and feel free to experiment in Workspaces or on your own computer.
#For this first task, create a function named num_teachers that takes a single argument, which will be a dictionary of Treehouse teachers and their courses.
#The num_teachers function should return an integer for how many teachers are in the dict.

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(teachers):
    count1 = 0
    for teachers in teachers:    # change the first teachers into teacher
        count1 += 1
    return count1
#---------------------------------------------------------------------------------------------------#
#Challenge Task 2 of 5
#That one wasn't too bad, right? Let's try something a bit more challenging.
#Create a new function named num_courses that will receive the same dictionary as its only argument.
#The function should return the total number of courses for all of the teachers.
def num_courses(teachers):
    count2 = 0
    for value in teachers.values():
        count2 += len(value)
    return count2
#---------------------------------------------------------------------------------------------------#
#Challenge Task 3 of 5
#Great work! OK, you're doing great so I'll keep increasing the difficulty.
#For this step, make another new function named courses that will, again, take the dictionary of teachers and courses.
#courses, though, should return a single list of all of the available courses in the dictionary. No teachers, just course names!

def courses(teachers):
    course_list = []
    for value in teachers.values():
        course_list += value
    return course_list
#---------------------------------------------------------------------------------------------------#
#Challenge Task 4 of 5
#Wow, I just can't stump you! OK, two more to go. I think this one's my favorite, though.
#Create a function named most_courses that takes our good ol' teacher dictionary.
#most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.

def most_courses(teachers):
    max_count = 0
    rockstar = ""
    for teacher, course_list in teachers.items():
        if len(course_list) > max_count:
            max_count = len(course_list)
            rockstar = teacher
    return rockstar
#---------------------------------------------------------------------------------------------------#
#Challenge Task 5 of 5
#It's official: you're awesome at Python dictionaries! One last task and then you can take a well-deserved break!
#In this last challenge, I want you to create a function named stats and it'll take our teacher dictionary as its only argument.
#stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats(teachers):
    outer_list = []
    for key in teachers:
        inner_list = []
        inner_list.append(key)
        inner_list.append(len(teachers[key]))
        outer_list.append(inner_list)
    return outer_list

