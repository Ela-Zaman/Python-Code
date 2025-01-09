from pathlib import Path

contents = "I Love Programming. \n"
contents += "I Love Creating new games. \n"
contents += "I also love working with data.\n"

path = Path("programming.txt")
path.write_text(contents)