'''The following program will print numbers that are divisible by 7 but
not multiples of 5 between 2000 and 3200 and in next case
will also ask for user input of the starting number and ending number to print the output 
based on user's choice of starting and ending numbers'''

#Part 1: fixed range i.e. 2000 to 3200
result = []

#defining fixed range
for num in range(2000, 3200):
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))
#to display the output of numbers seperated by comma
print(", ".join(result))

#Part 2:User defined range
#Asking for input range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

result = []

for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))

# Print as comma-separated string
print(", ".join(result))

#by Biplab Prasad Gajurel 25024641