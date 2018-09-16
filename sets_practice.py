# lists [,]
# dictionaries {:}
# strings "" or ''
# tuple (,) or tuple([1, 2, 3])

# One of the most common ways you'll see sets being used is to make some other iterable unique.
# For example, say you have a list of page numbers where terms appear in a book.
# Since some pages could contain multiple terms, you're likely to get repeats. In that case, you'll see people doing code like this:
# pages = list(set(pages))

# sets are mutable

set([1, 3, 5])
# creates the set {1, 3, 5}
{1, 3, 5}
# also creates the set {1, 3, 5}
type(set())

low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17) # adds single items
low_primes.update({19, 23}, {2, 29}) # adds multiple items
low_primes.add(15)
low_primes.remove(15)
low_primes.remove(100) # error if doesn't exist
low_primes.discard(100) # won't error if doesn't exist




# Challenge Task 1 of 3
# I think it's a good idea for you to experiment with sets since they're a very useful part of Python.
# Start by creating a set variable named songs that has three song titles in it.
# You can use any titles you want, just make sure they're three different strings.
songs = {"string1", "string2", "string3"}
# Challenge Task 2 of 3
# Awesome. Now use the .add() method to add the title "Treehouse Hula" to songs.
songs.add("Treehouse Hula")
# Challenge Task 3 of 3
# Alright, and last task. Use .update() to add the following two sets to your songs set.
# {"Python Two-Step", "Ruby Rhumba"}
# {"My PDF Files"}
songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})



# Here's yet another brief explanation of the common set operations:

# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
# (also: notice how those are using *others? That's a tuple of other sets. See, I told you that pattern was everywhere!)

set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
set1.union(set2)
set1 | set2
set1.difference(set2)
set2.difference(set1)
set1 - set2
set2 - set1
set1 ^ set2 
set2.symmetric_difference(set1)
set1.intersection(set2)
set1 & set2






# Challenge Task 1 of 2
# Let's write some functions to explore set math a bit more. 
# We're going to be using this COURSES dict in all of the examples. Don't change it, though!
# So, first, write a function named covers that accepts a single parameter, a set of topics. 
# Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.
# For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(set_of_topics):
    list_of_courses = []
    for key, value in COURSES.items():
        if value.intersection(set_of_topics):
            list_of_courses.append(key)
    return list_of_courses


# Challenge Task 2 of 2
# Great work!
# OK, let's create something a bit more refined. 
# Create a new function named covers_all that takes a single set as an argument. 
# Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. 
# Java Basics and PHP Basics would be excluded because they don't include both of those topics.


def covers_all(topics):
    courses_list = []    
    for course, values in COURSES.items():
        if(values & topics)  == topics:
            courses_list.append(course)

    return courses_list