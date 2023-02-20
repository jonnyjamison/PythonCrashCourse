""" A short program which stores a set of numbers and 
another program which reads them back into memory"""

import json 

numbers = [2, 3, 5, 7, 11, 13]

filename = 'Chapter10_Files_and_Exceptions/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) #'dump' allows us to store the numbers in the json file


