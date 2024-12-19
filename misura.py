import ROOT
import numpy as np
import math as m

e = np.array([])
erre = np.array([])
e_h = np.array([])
erre_h = np.array([])
h_k = np.array([])
errh_k = np.array([])
e_k = np.array([])
erre_k = np.array([])

file1 = open('e.dat','r')
file2 = open('e_h.dat','r')
file3 = open('h_k.dat','r')
file4 = open('e_k.dat','r')

files = [file1, file2, file3, file4]
cost = [e, e_h, h_k, e_k]
errcost = [erre, erre_h, errh_k, erre_k]

i = 0
'''
for file in files:   
    for line in file:
        str = line.split()
        if len(str)>0:
            if i == 0:
                e = np.append(e, float(str[0]))
                erre = np.append(erre, float(str[1]))
            if i == 1:
                e_h = np.append(e_h, float(str[0]))
                erre_h = np.append(erre_h, float(str[1]))
            if i == 2:
                h_k = np.append(h_k, float(str[0]))
                errh_k = np.append(errh_k, float(str[1]))
            if i == 3:
                e_k = np.append(e_k, float(str[0]))
                erre_k = np.append(erre_k, float(str[1]))                
    i += 1
'''
for file in files:   
    for line in file:
        str = line.split()
        if len(str)>0:
            cost[i] = np.append(cost[i], float(str[0]))
            errcost[i] = np.append(errcost[i], float(str[1]))  
    i += 1

e = cost[0]
erre = errcost[0]
e_h = cost[1]
erre_h = errcost[1]
h_k = cost[2]
errh_k = errcost[2]
e_k = cost[3]
erre_k = errcost[3]

#migliori valori
E = e[0]
E_H = e_h[5]
H_K = h_k[2]
E_K = e_k[12]

print("e:", e)
print("e_h:", e_h)
print("h_k:", h_k)
print("e_k:", e_k)
print("")
print("MIGLIORI VALORI")
print("e:", E)
print("e_h:", E_H)
print("h_k:", H_K)
print("e_k:", E_K)

