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

for i in v1:
    n1 = c1 * float(i)

    finaln1 = (c1 * kb) ** 0.5

    finaln2 = (c2 * ka) ** 0.5

    print(i, " -- ", finaln1, "  ", finaln2 )