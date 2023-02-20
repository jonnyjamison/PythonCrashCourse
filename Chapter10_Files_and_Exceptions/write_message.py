filename = 'programming.txt'

with open(filename, 'w') as file_object: #'w' means write mode - we can write to file
    #open automatically creates a file if it doesnt exist
    #be careful opening a file using 'w' as python will erase contents of file before returning it as object 
 file_object.write("I love programming.") #will write this message in the txt file

 #python can only write strings to files. To store numerical data, will have to convert it to string first

 with open(filename, 'a') as file_object: #'a' is append mode - will add below strings onto existing file 
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")