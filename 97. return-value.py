def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jime','hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    full_name= f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#make the middle name optional

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name= f"{first_name} {middle_name} {last_name}"
    else:
        full_name= f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'hooker')
print(musician)