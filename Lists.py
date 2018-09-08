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

for attendee in attendees:
    print(attendee)



books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]


def display_wishlist(display_name, wishes):
    print(display_name + ":")
    suggested_gift = wishes.pop(0)
    print("=======>", suggested_gift, "<=======")
    for wish in wishes:
        print("* " + wish)
    print()
    
display_wishlist("Books", books)
display_wishlist("Video Games", video_games)