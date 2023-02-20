import json

filename = 'Chapter10_Files_and_Exceptions/numbers.json'
with open(filename) as f:
    numbers = json.load(f) #will be assigned to variable name numbers
print(numbers)