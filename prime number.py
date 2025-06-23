lower=int(input("enter an lower range:"))
upper=int(input("enter an upper range:"))
print("prime numbers between",lower,"and",upper,"are:")
prime_numbers = ''
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            prime_numbers = prime_numbers+ str(num) + ' ' 
print (prime_numbers)            
