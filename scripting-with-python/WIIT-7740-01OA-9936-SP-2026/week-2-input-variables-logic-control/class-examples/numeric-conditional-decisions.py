LEGAL_VOTING_AGE = 18
age = 17

if age > LEGAL_VOTING_AGE:
    print("Individual can vote")
elif age < LEGAL_VOTING_AGE:
    print("Individual can not vote")
else:
    print("Individual's age is 18 and therefore voting is legal")