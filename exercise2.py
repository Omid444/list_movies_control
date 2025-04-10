
def sum_triangulars(numbers):
    result = 0
    result_list = []
    for number in numbers:
        result = 0
        for j in range(1,number+1):
            result += j
        result_list.append(result)
    return result_list

list_of_numbers = [6,5,0,12,7]
print(sum_triangulars(list_of_numbers))