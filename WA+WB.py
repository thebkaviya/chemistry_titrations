v1 = []
ph_values = []
for i in range(0,50+1):
    v1.append(round(i*0.001,4))
print (v1)

c1 = c2 = 1.0
v2 = 0.025

ka = 2 * (10**-5)
kb = 2 * (10**-5)


n2 = c2 * v2 

import math

for i in v1:
    n1 = c1 * float(i)

    finaln1 = ((c1 * kb) ** 0.5)*i

    finaln2 = ((c2 * ka) ** 0.5)*v2

    #print(i, " -- ", finaln1, "  ", finaln2 )

    if finaln1 == 0:
        ph = -1 * math.log(finaln2)
    
    elif finaln2 > finaln1:
        ph = math.log(ka) + math.log((finaln2 / (n2 - finaln2)) / (i + v2))

    elif finaln2 < finaln1:
        poh = math.log(kb) + math.log((finaln1 / (n1 - finaln1)) / (i + v2))
        ph = 14 - poh

    else:
        ph = 7

    ph_values.append(round(ph,4))

    print (i, "---", ph)


import matplotlib.pyplot as plt
# plt.plot(titration_volumes, pH_values)
plt.plot(v1, ph_values)
plt.xlabel('Titration volumes')
plt.ylabel('pH values')
plt.show()