from city_function import formatted_city_country

def test_city_country_population():
    """ Check whether the test city country """
    formatted_word = formatted_city_country('santiago', 'chile', '500000')
    assert formatted_word == "Santiago, Chile - Population 500000"