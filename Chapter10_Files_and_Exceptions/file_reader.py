with open('pi_digits.txt') as file_object: #open function returns an object representing the file
    #in this example, it is returns as file_object
    #The 'with' keyword automatically closes the file once it is no longer needed - notice how you dont need to call close. Python will work this out for us. 
    #When you use with, the file object returned by open() is only available inside the with block that contains it.
    contents = file_object.read() #Read will store file contents in a string using read()
    print(contents)

#To work with file outside of with block:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

# can use print(contents.rstrip()) to remove empty line at end of string
#rstrip removes any whitespace from right side of a string
#may have to provide full filepath, just like matlab. or can specifcy it in relation to project directory, just like matlab

#To add contents all to one line:
pi_string = ''
for line in lines:
    pi_string += line.strip()