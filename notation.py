nums = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def convert_to_base(number, dev):
    if dev > number:
        return str(nums[number % dev]) if number % dev > 9 else str(number % dev)
    return convert_to_base(number // dev, dev) + (str(nums[number % dev]) if number % dev > 9 else str(number % dev))

first = int(input('Введите число: '))
second = int(input('Введите в какую систему его перевести: '))

print(convert_to_base(255, 16))