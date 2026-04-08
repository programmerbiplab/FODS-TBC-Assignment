'''The following program takes input of two numbers from the user and
finds the prime numbers between them and 
also finds the sum of all the displayed prime numbers'''

#taking input of starting and ending number to find prime numbers between them
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

#The below variable will keep track of sum of prime numbers initially starts at zero
prime_sum = 0

#simple message before listing the actual numbers and displaying the output
print("Prime numbers between", start, "and", end, "are:")

#starts the loop, checks each number one by one if prime or not
for num in range(start, end + 1):
    if num > 1:
        #assuming the number is prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                #If num is divisible by i (i.e., remainder is 0), then it's not prime
                is_prime = False
                break
        #After the inner loop, we check if is_prime is still True
        if is_prime:
            print(num, end=' ')
            prime_sum += num
print("\nSum of all prime numbers:", prime_sum)

#by Biplab Prasad Gajurel 25024641
