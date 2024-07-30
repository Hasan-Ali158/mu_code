def main():
	n = int(input("Enter number of departments :   "))
	file = open("expenses.txt")
	for i in range(n):
		s = ""
		a = file.readline()
		j = 0
		while a[j] != "\n":
				s = s + a[j]
				j = j + 1
		summ = 0
		for k in range(7):
			n = file.readline()
			summ = summ + int(n)
		
		print(s,":",summ)

main()
