import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #class name called NamesTestCase MUST inherit from unittest.TestCase so Python knows how to run the tests
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self): #ANY METHOD THAT BEGINS WITH test_ will be automatically ran when test_name_function IS RAN
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #This line translates to: compare formatted_name to the string Janis Joplin - if not equal, create an error

    def test_first_last_middle_name(self): #METHOD MUST START WITH test_
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')



if __name__ == '__main__': #if this file is being ran as the main program, name will be equal to 'main'
    unittest.main()