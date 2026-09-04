#1
num_str = input("Введите натуральное число: ")

sumA = 0

for digit_char in num_str:
    digit = int(digit_char)
    if digit % 2 != 0:
        sumA += digit

print("Сумма нечётных цифр:", sumA)

#2
text = input("Введите строку: ")
words = text.split()
count_odd = 0

for word in words:
    if len(word) % 2 != 0:
        count_odd += 1

print("Количество слов с нечётным числом букв:", count_odd)