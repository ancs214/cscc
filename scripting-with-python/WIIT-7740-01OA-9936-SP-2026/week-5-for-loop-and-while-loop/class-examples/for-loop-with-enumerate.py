items = [2,4,6,8,0,1,3,5,7,9]
item_index = 0

# instead of just handing you the value, enumerate() hands you a pair (a tuple) containing (index, value)
for item_index, item in enumerate(items):
    print('List contains the number', item, 'at index', item_index)