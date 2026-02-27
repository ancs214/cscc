my_stock = {
    "Product": "Earbuds",
    "Price": 200,
    "Quantity": 50,
    "InStock": "Yes"
}

print(my_stock)

print("My dictionary length is", len(my_stock), "key/value pairs")

print("The keys in my dictionary are", my_stock.keys())

print("The values in my dictionary are", my_stock.values())

# add a key/value pair to dictionary
my_stock["Discontinued"] = "No"
print(my_stock)

# both 'for statements' below iterate over a dictionary
# this for statement will loop through its KEYS to get the value
for key in my_stock:
    value = my_stock[key]
    print("Key is", key, ": Value is", value)
#this for statement uses the .items() method to upack BOTH the key and value as a tuple
for key, value in my_stock.items():
    print(key, value)

# delete a key/value pair from dictionary
del my_stock["InStock"]
print(my_stock)

# empty or clear dictionary
print(my_stock.clear())
