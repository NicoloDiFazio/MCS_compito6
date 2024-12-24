import ROOT
import numpy as np
import math as m

from   iminuit import Minuit
import matplotlib.pyplot as plt

#definisco le funzioni di minuit
#def f(x,p):
#    return p[1]*x+p[0]

def fcn(par):
    chi2 = ((par[0]-mis[0])/err[0])**2 + ((par[0]/par[1]-mis[1])/err[1])**2 + ((par[1]/par[2]-mis[2])/err[2])**2 + ((par[0]/par[2]-mis[3])/err[3])**2
    return chi2

#X2 =((e-(e)mis)/s(e))2+((e/h-(e/h)mis)/s(e/h))2+((h/k-(h/k)mis)/s(h/k))2+((e/k-(e/k)mis)/s(e/k))2
#raccolgo i dati
E = np.array([])
E_H = np.array([])
H_K = np.array([])
E_K = np.array([])
errE = np.array([])
errE_H = np.array([])
errH_K = np.array([])
errE_K = np.array([])

file1 = open('e.dat','r')
file2 = open('e_h.dat','r')
file3 = open('h_k.dat','r')
file4 = open('e_k.dat','r')

files = [file1, file2, file3, file4]
cost = [E, E_H, H_K, E_K]
errcost = [errE, errE_H, errH_K, errE_K]

i = 0

for file in files:   
    for line in file:
        str = line.split()
        if len(str)>0:
            cost[i] = np.append(cost[i], float(str[0]))
            errcost[i] = np.append(errcost[i], float(str[1]))  
    i += 1

E = cost[0]
E_H = cost[1]
H_K = cost[2]
E_K = cost[3]

errE = errcost[0]
errE_H = errcost[1]
errH_K = errcost[2]
errE_K = errcost[3]

#seleziono i migliori valori
e = E[0]
e_h = E_H[5]
h_k = H_K[2]
e_k = E_K[12]

erre = errE[0]
erre_h = errE_H[5]
errh_k = errH_K[2]
erre_k = errE_K[12]
'''
print("e:", E)
print("e_h:", E_H)
print("h_k:", H_K)
print("e_k:", E_K)
print("")
'''
print("MIGLIORI VALORI")
print("e: %f +- %f" %(e, erre))
print("e_h: %f +- %f" %(e_h, erre_h))
print("h_k: %f +- %f" %(h_k, errh_k))
print("e_k: %f +- %f" %(e_k, erre_k))

par = np.array([1.6e-19, 6.6e-34, 1.2e-23])
mis = np.array([e, e_h, h_k, e_k])
err = np.array([erre, erre_h, errh_k, erre_k])
m = Minuit(fcn, par)
m.migrad()

print("")
print("Valori Minimizzati")
print(" e = %f +- %f " %(m.values[0], m.errors[0]))
print(" h = %f +- %f " %(m.values[1], m.errors[1]))
print(" k = %f +- %f " %(m.values[2], m.errors[2]))


