def is_divisible_by(number, by):
	return number % by

def is_prime(number):
	if number !=0 and number != 1:
		for i in range(2,int(number **0.5)+1):
			result = is_divisible_by(number, i)
			if result == 0:
				return False
		else:
			return True
	return False

def print_prime_numbers(list_of_prime_numbers):
	for number in list_of_prime_numbers:
		print(f'The number {number} is prime')

def primes_in_range(start, end):
	prime_list = []
	for i in range(start,end):
		current_number = is_prime(i)
		if current_number:
			prime_list.append(i)
	print_prime_numbers(prime_list)


def main():
	first_number = int(input('please enter start range: '))
	second_number = int(input('please enter second number: '))
	primes_in_range(first_number,second_number)

if __name__ == '__main__':
	main()


