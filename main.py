def decimal_to_binary(num): #this is our procedure to convert decimal to binary
  binary_num = "" #this sets up our empty string we can use to print later on
  while num > 0: #this loop will go through the number and add the digits to the binary_num string
    binary_num = str(num % 2) + binary_num #this will add the digits to the binary_num string
    num = num // 2 #this will divide the number by 2 and then add it to the number
  return binary_num 

def binary_to_decimal(num): #this is our procedure to convert binary numbers to decimal numbers
  decimal = 0 #sets decimal to 0. we will print this later on
  for digit in num: #this loop will go through every digit in the user input "num"
    decimal = decimal * 2 + int(digit) #this will take the decimal and multiply it by 2 and add the digit to the decimal
  return decimal

def compare_binary(num1, num2): #this is our comparing binary procedure where it will compare two binary numbers that the user gives us
  if num1 == num2: #if the two binary numbers are the same then it will convert the binary numbers to decimals and print
    print(str(binary_to_decimal(num1)) + ' , ' + str(binary_to_decimal(num2)))
  else:
    final = binary_to_decimal(num1) #this will convert the first binary number to decimal using the binary_to_decimal procedure
    final2 = binary_to_decimal(num2) #this will convert the second binary number to decimal using the binary_to_decimal procedure
    print(str(final) + ' , ' + str(final2)) 
    print(str(num1) + ' , ' + str(num2)) #lines 20 and 21 will print the original user inputs

print('Choose an Action:') #asking the user for what action to choose
print('Press 1 to convert to decimal to binary')
print('Press 2 to convert to binary to decimal')
print('Press 3 to compare binary numbers')
answer = input() #this captures the user input

if answer == '1':
  print('Enter a decimal number:')
  num = input()
  if num.isdigit(): #checks to see if the user input is a valid digit
    num = int(num) #sets the string to an integer so the procedure can use it 
    final = decimal_to_binary(num) #sets a variable equal to the procedure
    print()
    print(str(num) + ' converted to binary is ' + str(final)) #printing the binary number
  else:
    print('Please enter a valid decimal number. Try again.') #if the user input is not a valid digit then print the error message
elif answer == '2':
  print('Enter a binary number:')
  num = input()
  if num.isnumeric():
    if any([int(i) > 1 for i in num]): #this will check to see if every single digit in the user input is bigger than 1, if so then it is not a binary number
      print('Please enter a valid binary number. Try again') #this will tell users that their input is not in binary form
    else:
      print()
      print(str(num) + ' converted to decimal is ' + str(binary_to_decimal(num))) #printing the decimal number
  else:
    print('Please enter a valid binary number. Try again') #if the user input is anything but a number then it will print an error message
elif answer == '3':
  print('Enter a binary number.') 
  num1 = input()
  print('Enter another binary number.')
  num2 = input()
  if num1.isnumeric() and num2.isnumeric(): #if both user inputs are in fact numbers, then it will move onto the next line of code
    if any([int(i) > 1 for i in num1 and num2]): #this will check to see if every single digit in the user inputs is bigger than 1, if so then it is not a binary number and tell the user
      print('Please enter a valid binary number. Try again')
    else:
      print()
      compare_binary(num1, num2) #calling the procedure compare_binary
  else:
    print('Please enter a valid binary number. Try again') #if the user input is not a binary number then it will notify the user 
else:
  print('Not a valid option. Try again.') #this accounts for any user input that is not a valid option