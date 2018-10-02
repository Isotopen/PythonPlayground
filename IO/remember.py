import sys

def rememberer(thing):
#     # open file
    with open("database.txt", "a") as file:
        # write thing to file
        file.write(thing+"\n")


def show():
    # open file
    with open("database.txt", "r") as file:
        for line in file:
            print(line)
    # print out each line in file
    # close file
    pass


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))
    rememberer(input("What should I remember? "))