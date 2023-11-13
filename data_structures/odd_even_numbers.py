# Q. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
odd_nums = []
max_num = int(input("Enter a number: "))
for i in range(1, max_num + 1):
	if i % 2 != 0:
		odd_nums.append(i)
		
print(odd_nums)