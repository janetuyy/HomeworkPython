# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# в txt формате
print("WELCOME TO THE PHONEBOOK DIRECTORY")

with open('phonebook.txt', 'a+') as phonebook:
    phonebook.close()

# defining main menu
def main_menu():
    print("\nMAIN MENU\n")
    print("1. Show my contacts")
    print("2. Add a new contact")
    print("3. Search the contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        with open('phonebook.txt', 'r') as phonebook:
            content = phonebook.read()
            if len(content) == 0:
                print("u don' have any contacts in ur phonebook")
            else:
                print(content)
            phonebook.close()
        enter = input("Press Enter to continue...")
        main_menu()
    elif choice == "2":
        newcontact()
        enter = input("Press Enter to continue...")
        main_menu()
    elif choice == "3":
        searchcontact()
        enter = input("Press Enter to continue...")
        main_menu()
    elif choice == "4":
        print("See u later!")
    else:
        enter = input("Please provide a valid input!\n Press Enter to continue...")
        main_menu()

    # defining search function


def searchcontact():
    searchname = input("Enter First name for Searching contact record: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open('phonebook.txt', "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Your Required Contact Record is:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print("The Searched Contact is not available in the Phone Book", searchname)

    # first name


def input_firstname():
    first = input("Enter your First Name: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# last name
def input_lastname():
    last = input("Enter your Last Name: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# storing the new contact details
def newcontact():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Enter a Phone number: ")
    emailID = input("Enter an E-mail Address: ")
    contactDetails = ("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID + "]\n")
    myfile = open('phonebook.txt', "a")
    myfile.write(contactDetails)
    print("The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!")


main_menu()
