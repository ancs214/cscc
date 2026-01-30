def greet_users(names):
    """Print simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['ashley-noel', 'erica', 'hannah', 'ty']
greet_users(usernames)