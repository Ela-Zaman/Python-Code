glossary={
    "for": "used for loop",
    "if":"conditional statements",
    "range()":"use to generate numbers between range",
    "list": "combination of value",
    "tuple": "value cannot change",
}

for key,value in glossary.items():
    print(f"{key} works as {value}")

glossary["dictionary"]="stores key value pairs"
glossary["del"]="delate items"
glossary["set"]="stores unique value"
glossary["items()"]="used to loop through dictionary"
glossary["print()"]="prints the output"

for key,value in glossary.items():
    print(f"{key} works as {value}")