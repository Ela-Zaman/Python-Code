from pathlib import Path


def content_of_file(filename):
    path=Path(filename)
    try:
        content=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        lines=content.split()
        print(f"The {filename} contains: ")
        for line in lines:
            print(line)

filenames= ['cats.txt', 'dogs.txt', 'animal.txt']

for file in filenames:
    content_of_file(file)