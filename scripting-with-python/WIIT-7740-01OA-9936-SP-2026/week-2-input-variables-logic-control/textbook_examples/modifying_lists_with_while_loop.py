#a for loop is effective to loop through a list, but you shouldn't modify a list inside a for loop
#python will have trouble keeping track of the items in the list

#moving items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#while loop will verify each user and add to confirmed user list until no more unconfirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#removing all instances of specific value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary with user input
#a list is an ordered collection of items accessed by an integer index, while a dictionary
# is an unordered collection of unique key-value pairs accessed by a specific key

#empty dictionary
responses = {}
#flag to indicate when to end program
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    #standard way to add/update information in a python dictionary
    #"key:value" pair will become "name:response" and dictionary is called "responses"
    responses[name] = response

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

    #polling complete. show results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")