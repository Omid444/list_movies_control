

def summer_user_input_numbers():
    total_number = 0
    while total_number <= 1000:
        numbers = int(input('Enter your number: '))
        total_number += numbers
    return total_number

def print_sum_numbers(total_numbers):
    return print(f'Final sum: {total_numbers}')

def main():
  sum_numbers = summer_user_input_numbers()
  print_sum_numbers(sum_numbers)


if __name__ == "__main__":
    main()