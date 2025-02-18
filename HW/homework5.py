def fast_power(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  
            result *= a
        a *= a  
        n //= 2  
    return result

print(fast_power(20, 10))  
print(fast_power(3, 5))   
