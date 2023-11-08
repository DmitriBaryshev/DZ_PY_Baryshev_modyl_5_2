# Задание 1
def p(l):
    res = 1
    for i in l:
        res *= i
    return res
print(p([1, 2, 3, 4]))
# Задание 2
numbers = [4, 8, 2, 6, 500, 9, 5]
min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
print(min_num)
# Задание 3
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17]
def is_prime(number):
    if number == 1:
        return True
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True
primes_count = 0
for number in l1:
    primes_count += is_prime(number)
print(primes_count)
# Задание 4
def f(n, l):
    r = len(l)
    while True:
        if l.count(n) == 0:
            break
        l.remove(n)
    return r - len(l)
print(f(9,[2, 3, 5, 5, 5, 9, 5, 8, 7]))
# Задание 5
def combine_lists(list1, list2):
    combined_list = list1 + list2
    return combined_list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = combine_lists(list1, list2)
print(result)
# Задание 6
def calculate_power_of_elements(lst, power):
    result = [i ** power for i in lst]
    return result
numbers = [1, 2, 3, 4, 5]
power = 3
result = calculate_power_of_elements(numbers, power)
print(result) 