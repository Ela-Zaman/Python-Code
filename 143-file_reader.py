from pathlib import Path

path=Path('text_files/filename.txt')
contents =path.read_text()
print(contents) 

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string+=line.lstrip()

print(pi_string)
print(len(pi_string))

list = '123456'
print(list[:4])
path=(f"{pi_string[:52]}")



