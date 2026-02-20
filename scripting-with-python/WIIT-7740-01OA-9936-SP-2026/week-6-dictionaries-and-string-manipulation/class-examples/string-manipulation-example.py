str_1 = "Die Hard is a Christmas movie...PERIOD!!!"
str_2 = " And so was Lethal Weapon!"
str_3 = "Rose could have scooted her behind over on that door!"
str_4 = "Michael Corelone gained the entire world and lost his soul in the process."

print(str_4.count("the", 21, 78))
print(str_1.lower())
print(str_2.upper())

str_5 = str_1 + str_2
print(str_5)

if "Scooted".lower() in str_3:
    print("Yes!")

print(str_1.index("Hard", 4, 16))
print(str_3.isascii())
print(str_3.isnumeric())
