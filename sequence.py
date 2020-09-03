#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#1. ask for three consecutive numbers (123)
#2. add them together to get the fourth number (6)
#3. take the fourth (newest) number and add it together with the 2 numbers ahead of it (2+3+6=11)
#4. repeat step 3 n times

n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_int = 1
second_int = 2
third_int = 3
sum = 0

for n in range (1,n+1):
	if n < 4:
		print(n)
	else:
		sum = first_int + second_int + third_int
		print(sum)
		first_int = second_int
		second_int = third_int
		third_int = sum