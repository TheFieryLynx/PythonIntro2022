import math
k = int(input())      

if k == 0 or k == 1:
    print(k)
else:
    deg = 1
    x = 0
    while (10 * x + k) * k != deg * k + x:
        deg *= 10
        x = (deg * k  - k * k) // (10 * k - 1)
    print(10 * x + k)