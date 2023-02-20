print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
            break
    
    
    try: #Only the piece of code that might cause an error should go in try block
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError: #tells python how to respond when zero division error occurs. This means user will never have to see the traceback
        print("You can't divide by 0!")
    else: #if the try block doesnt cause an error, execute this
        print(answer) 
    
    #because it is within a while loop, will print the "cant divide by 0" message and continue to run the program