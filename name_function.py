# To upgrade 
# python -m pip install --upgrade {package_name}
# pytest 
# python -m pip install --user pytest

def get_formatted_name(first,last, middle=""):
    """Generate a neatly formatted full name. """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



