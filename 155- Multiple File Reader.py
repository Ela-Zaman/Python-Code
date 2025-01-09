from pathlib import Path

filenames = ['alice.txt','moby_dick.txt','guest_book.txt','learning_python.txt']

def count_words(filename):
    """Count the approximate number of words in a file."""
    for file in filename:
        path=Path(file)
        try:
            content=path.read_text(encoding = 'utf-8')
        except FileNotFoundError:
            print(f"The {file} is not found on the system")
        else:
            lines = content.split()
            words=len(lines)
            print(f"The {file} has {words} words")


count_words(filenames)

#The efficient name in count_words()

def count_words_2(filename):
    try:
        path=Path(filename)
        content = path.read_text(encoding = "utf-8")
    except FileNotFoundError:
        print(f"The {filename} is not available")
    else:
        
        lines = content.split()
        words = len(lines)
        print(f"The {filename} has {words} words")

filenames = ['alice.txt','moby_dick.txt','guest_book.txt','learning_python.txt']

for file in filenames:
    count_words_2(file)