Saul
Resendiz		

			WEEk 6 LAB
	
	QUESTION 1:

myfile = open('numbers.txt', 'r')

for line in myfile:
    number = int(line)
    print(number)

myfile.close()

	QUESTION 2:

user_file_name = input("Enter the name of file: ")

try:
    #opening and reading file lines
    with open(user_file_name, 'r') as myfile:
        lines = 0   #Line counter

        for line in myfile:
            print(line.strip())  
            lines += 1
            if (lines == 5) :   #Only reading up to 5 lines
                break

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
	

	QUESTION 3: 

user_file_name = input("Enter file name: ")

try:
    #opening and reading file lines
    with open(user_file_name, 'r') as myfile:
        line_numbering = 1  #Line number counter

        for line in myfile:
            print(f"Line #: {line_numbering}")
            line_numbering += 1

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")


	QUESTION 4:

user_file_name = 'names.txt'

item_count = 0

try:
    # counting every line w strings
    with open(user_file_name, 'r') as myfile:
        for line in myfile:
             line = line.strip() 
            if line:  # check if name string exists before counting
               item_count  += 1  

    # displaying item count
    print(f"The total number of names in the file is: {item_count}")

except FileNotFoundError:
    print(f"The file {file_name} does not exist.")


	QUESTION 5:

user_file_name = 'numbers.txt'
total_ints = 0  

try:
    with open(user_file_name, 'r') as myfile:
        for line in myfile:
            number = int(line.strip())  #converting the number to int type
            total_ints += number     #add to total

    print(f"TOTAL SUM: {total_ints}")

except FileNotFoundError:
    print("The file does not exist.")
except ValueError:
    print("The file contains non-integer values.")

