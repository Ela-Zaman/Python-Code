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

path2 = Path('one-million.txt')
contents2 = path2.read_text()
lines_2 = contents2.splitlines()
pi_string_2=""
for line in lines_2:
    pi_string_2+=line

print(f"{pi_string_2[:52]}....")
print(len(pi_string_2))



