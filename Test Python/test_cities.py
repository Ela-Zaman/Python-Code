from city_function import formatted_city_country
def test_city_country():
    """Check whether the Santiaogo, Chili passes the test"""

    formatted_test = formatted_city_country('santiago', 'chili')
    assert formatted_test == 'Santiago, Chili'
