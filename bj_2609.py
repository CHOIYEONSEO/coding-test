def gcd(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

num1, num2 = map(int, input().split())
gcd_result = gcd(num1, num2)
lcm_result = (num1 // gcd_result) * (num2 // gcd_result) * gcd_result

print(gcd_result)
print(lcm_result)