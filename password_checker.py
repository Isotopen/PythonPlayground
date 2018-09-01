# Password checking app
password = input("Please enter the super secret password: ")
attempt_count = 1
while password != 'opensesame':
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to secret town")