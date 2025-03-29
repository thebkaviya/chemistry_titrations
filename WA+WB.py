v1 = []
ph_values = []
for i in range(0,50+1):
    v1.append(round(i*0.001,4))
print (v1)

c1 = c2 = 1.0
v2 = 0.025

ka = 0.00002
kb = 0.00002


n2 = c2 * v2 

import math

for i in v1:
    n1 = c1 * float(i)

    finaln1 = (c1 * kb) ** 0.5

    finaln2 = (c2 * ka) ** 0.5

    print(i, " -- ", finaln1, "  ", finaln2 )

    if finaln2 > finaln1:
        ph = -1 * math.log((finaln2 - finaln1) / (float(i + v2)))

    elif finaln2 < finaln1:
        poh = -1 * math.log((finaln1 - finaln2) / (float(i + v2)))
        ph = 14 - poh

    elif finaln2 == finaln1:
        ph = 0000000000

    else:
        ph = -1 * math.log(ka ** 0.5)

    print (i, "---", ph)