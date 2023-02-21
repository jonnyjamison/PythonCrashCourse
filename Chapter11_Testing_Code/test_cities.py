import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase): #class MUST inherit from unittest.TestCase so Python knows how to run the tests
    """Tests for 'city_functions.py'."""

    def test_city_country(self): #ANY METHOD THAT BEGINS WITH test_ will be automatically ran when test_name_function IS RAN
        """Does combinations like Belfast, NI work?"""
        city_combo = city_country('Belfast', 'NI')
        self.assertEqual(city_combo, 'Belfast, NI')

    def test_city_country_population(self): #ANY METHOD THAT BEGINS WITH test_ will be automatically ran when test_name_function IS RAN
        """Does combinations like Belfast, NI, 1000 work?"""
        city_combo = city_country('Belfast', 'NI', '10000')
        self.assertEqual(city_combo, 'Belfast, NI - population: 10000')


if __name__ == '__main__': #if this file is being ran as the main program, name will be equal to 'main'
    unittest.main()