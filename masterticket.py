TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    num_tickets = input("Hello {}! How many tickets would you like?  ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! That's not a valid value. {}. Try again...".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("{}, that will cost ${}".format(name, amount_due))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are all sold out!!! :(")