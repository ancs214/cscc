#in conditional tests, "None" evaluates to False. if the user does
#not input an age, python will not add it to the dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age

    return person

musician = build_person('ashley-noel', 'swarn', 38)
print(musician)


