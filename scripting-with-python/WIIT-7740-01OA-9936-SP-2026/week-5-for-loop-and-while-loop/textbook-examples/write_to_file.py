from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

# if the file that path points to doesn't already exist, Python will create a new file
path = Path('programming.txt')
path.write_text(contents)


