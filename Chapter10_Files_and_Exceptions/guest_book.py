guest_array = []
guest_name = " "

while guest_name != "done":

    guest_name = input("Please enter guest's Name: ")
    if guest_name != "done":
        guest_array.append(guest_name)
    else:
        break


filename = 'Chapter10_Files_and_Exceptions/guest_book.txt'

with open(filename, 'a') as guest_book:
    for guest in guest_array:
        guest_book.write(guest + "\n")

with open(filename, 'r') as guest_book:
    contents = guest_book.read()
    print(contents)