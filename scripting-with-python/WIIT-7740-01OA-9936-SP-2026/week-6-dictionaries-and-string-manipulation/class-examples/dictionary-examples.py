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

# iterate over a dictionary
for key in my_stock:
    value = my_stock[key]
    print("Key is", key, ": Value is", value)

for key, value in my_stock.items():
    print(key, value)

# delete a key/value pair from dictionary
del my_stock["InStock"]
print(my_stock)

# empty or clear dictionary
print(my_stock.clear())


