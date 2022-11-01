#  a program that will take in any number of integers from a user and characterise into either an prime or an non-prime list 

print  ('''WELCOME...
           This program will carecterise each number provided by the user into PRIME and NON-PRIME number ''') 

# this code will print the given message

list = [int(number) for number in input("Enter any number \n").split(',')] #this code is for creating the list and woud seperate each number with comma
prime_list = []     # list for prime numbers
non_prime_list = []     # list for prime numbers


# Determine whether each number on the list is a prime number or not, and then add it to the list of prime numbers or leave it off.
for number in list:
    count = 0  #this is the code which declares the variable to count from 0

    for j in range(1 , number) :

     if number%j ==0:   #If the number is divisible by anything besides one and itself
        count +=1 #this adds one to the count

        if count == 1:    #if count is 1, means there is no other factor   
            prime_list.append(number)   #this adds the number to the list of the prime numbers
        else:
            non_prime_list.append(number)   #this adds the number to the list of the non-prime numbers
print("\nThe prime numbers are:")   #prints the given message
print(prime_list, sep = ", ")   #print the list of prime numbers where each number separated by comma

print("The non-prime numbers are:")     #prints the given message
print(non_prime_list, sep = ", ")   #print the list of prime numbers where each number separated by comma 
        

