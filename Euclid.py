first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

def gcd(a, b):
    if a == 0 or b == 0: 
        return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)
        
print(f'НОД чисел {first} и {second}: {gcd(first, second)}')