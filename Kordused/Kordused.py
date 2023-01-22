from random import *

#3
N=randint(1, 10)
p=0 # p - positive

for i in range(N):
    number= randint(-10, 10) # generate a random number between -10 and 10
    if number > 0:
        p+= 1 

print("Number of positive numbers:", p)

#2
R=int(input("Enter a number: "))
n= 1
for i in range(1, R+1, 2):
    n*=i
print(n)


#1
n=int(input("Enter a number (1-9): "))
p=" *   \n  ***  \n ***** \n*******\n   *" 
for i in range(n):
    print(p, end=" ")

