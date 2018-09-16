# dictionairies  {:}
player = {"name": "Douglas", "remaining_lives": 3, "levels": [1, 2, 3, 4], "items": {"pork": "5"}}
course_minutes = {"Name" : "Kenneth", "Course time" : 100, "Class" : "Python", "Job" : "Teacher"}

           

# Print the keys only
for key in course_minutes.keys():
    print(key)

# Print the values only
for value in course_minutes.values():
    print(value)

# Print the keys and values (tuples)
for item in course_minutes.items():
    print(item)