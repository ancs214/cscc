LEGAL_VOTING_AGE = 18

print("Please enter an age.")
age = int(input())

if age > LEGAL_VOTING_AGE:
    print("Individual can vote")
elif age < LEGAL_VOTING_AGE:
    print("Individual can not vote")
else:
    print("Individual's age is 18 and therefore voting is legal")

