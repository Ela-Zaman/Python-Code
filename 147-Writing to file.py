#python can only write strings to file

from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming. ")
path.write_text("Ela loves everything")
