# Write your solution for 1.4 here!


def is_prime(x):
	i=1
	for i in range(x):
		i+=1
	
		if x%i==0:
			return("True")

y=0
num = int(input("Enter a number: "))
print(is_prime(num))