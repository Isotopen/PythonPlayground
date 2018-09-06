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


attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently")