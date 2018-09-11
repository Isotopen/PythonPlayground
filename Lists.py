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
