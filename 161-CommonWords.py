from pathlib import Path

path = Path("alice.txt")
content = path.read_text(encoding='utf-8')

content=content.lower()

alice = content.count('alice')
the = content.count('the')
real_the = content.count('the ')
print(f"The string alice appears {alice} times in alice.txt ")
print(f"The string the appears {the} times in alice.txt ")
print(f"The string 'the ' appears {real_the} times in alice.txt ")