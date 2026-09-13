num = input("Введите натуральное число: ")

sumA = 0

for digit_char in num:
    digit = int(digit_char)
    if digit % 2 != 0:
        sumA += digit

print("Сумма нечётных цифр:", sumA)

s = input("\nВведите строку: ")

words = s.split()
count = 0

for word in words:
    letters = sum(ch.isalpha() for ch in word) 
    if letters % 2 != 0:
        count += 1

print("Количество слов с нечетным числом букв:", count)