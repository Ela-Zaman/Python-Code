from pathlib import Path

def count_words_2(filename):
    try:
        path=Path(filename)
        content = path.read_text(encoding = "utf-8")
    except FileNotFoundError:
        pass
    else:
        
        lines = content.split()
        words = len(lines)
        print(f"The {filename} has {words} words")

filenames = ['alice.txt','moby_dick.txt','guest_book.txt','learning_python.txt']

for file in filenames:
    count_words_2(file)

