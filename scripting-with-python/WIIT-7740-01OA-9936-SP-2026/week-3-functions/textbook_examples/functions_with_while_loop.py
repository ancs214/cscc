
#using a function with a while loop
def get_formatted_name(first_name,last_name):
    """Return full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#using "while True" creates an infinite while loop that will never
#become false on its own
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit.)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break
    #plug f_name and l_name values into our function
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def make_album(artist, album, songs=None):
    """Return a list of music albums with artist and number of songs"""
    album_info = {'artist':artist, 'album':album}
    if songs:
        album_info['songs'] = songs

    return album_info

album = make_album('green day', 'american idiot', '12')
print(album)
album = make_album('green day', 'dookie', '10')
print(album)