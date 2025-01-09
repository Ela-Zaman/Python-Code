from pathlib import Path

message = "I really like dogs."
r = message.replace("dog","cat")
print(r)

path = Path("learning_python.txt")

replaced_content = path.read_text().lower().replace("python", "C")
print(replaced_content)
