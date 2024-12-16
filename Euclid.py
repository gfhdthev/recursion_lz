def gcd(a, b):
    if a == 0 or b == 0: 
        return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)
        
print(gcd(15, 37))