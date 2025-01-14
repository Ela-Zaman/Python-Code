def formatted_city_country(city,country,population=""):
    

    if population != "":
        formatted_name = f"{city}, {country} - population {population}"
    else:
        formatted_name = f"{city}, {country}"


    return formatted_name.title()

print(formatted_city_country('Santiago', 'Chile',1000))




