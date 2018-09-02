TICKET_PRICE = 10

tickets_remaining = 100  

# Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
name = input("What is your name?  ")

# Prompt the user by name and ask how many tickets they would like
num_tickets = input("Hello {}! How many tickets would you like?  ".format(name))
num_tickets = int(num_tickets)

# Calculcate the price (number of tickets multiplied by the price) and assign it to a variable
amount_due = TICKET_PRICE * num_tickets

# Output the price to the screen
print("{}, that will cost ${}.  ".format(name, amount_due))