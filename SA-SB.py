v1 = []
for i in range(0,50+1):
    v1.append(round(i*0.001,4))
print (v1)

c1 = c2 = 1.0
v2 = 0.025

n2 = c1 * v2
 


import math

for i in v1:
    n1 = c1 * float(i)

    if n1 == 0:
        ph = -1*math.log(n2 / )

    elif n2 < n1:
        ph = -1 * math.log ((n2 - n1) / ( i + v2)  )

    elif n2 == n1:
        ph = 7

    # else:
    #     poh = -1 * math.log ((n1 - n2) / (i + v2))
    #     ph = 14 - poh

    print(i, "---", round(ph, 4))

