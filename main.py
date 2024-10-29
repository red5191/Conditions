sum_even, even = 0, 0

while even < 100:
    sum_even += even
    even += 2

print(f'Сумма всех четных от 1 о 100: {sum_even}')

print(f'Квадраты нечетных от 1 до 10: {[odd ** 2 for odd in range(1, 10, 2)]}')

count_tries = 0

while True:
    try:
        input_text = int(input('Напиши отрицательное число '))
        if input_text < 0:
            count_tries += 1
            break
        else:
            count_tries +=1
    except ValueError:
        continue

print(f'Было введено {count_tries} чисел')