from pathlib import Path

path = Path("learning_python.txt")

content=path.read_text()
lines=content.splitlines()
print(content)

while lines:
    line=lines.pop()
    print(line)