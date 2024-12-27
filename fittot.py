import ROOT
import numpy as np
import math as m
from   iminuit import Minuit
import matplotlib.pyplot as plt
import scipy.constants as c

#valori delle costanti con scipy
ce = c.e
ch = c.h
ck = c.k
'''
def fcn(par):
    chi2e   = ((mis[0] - par[0])/err[0])**2
    chi2e_h = ((mis[1] - par[0]/par[1])/err[1])**2
    chi2h_k = ((mis[2] - par[1]/par[2])/err[2])**2
    chi2e_k = ((mis[3] - par[0]/par[2])/err[3])**2
    chi2    = (chi2e + chi2e_h + chi2h_k + chi2e_k)
    return chi2
'''
def fcn(par):
    chi2e   = 0
    chi2e_h = 0
    chi2h_k = 0
    chi2e_k = 0
    chi2    = 0
    chi2e   = ((E - par[0])/sE)**2
    for i in range(0, len(E_H)):
        chi2e_h = ((E_H[i] - par[0]/par[1])/sE_H[i])**2
    for i in range(0, len(H_K)):
        chi2h_k = ((H_K[i] - par[1]/par[2])/sH_K[i])**2
    for i in range(0, len(E_K)):
        chi2e_k = ((E_K[i] - par[0]/par[2])/sE_K[i])**2
    chi2    = (chi2e + chi2e_h + chi2h_k + chi2e_k)
    return chi2

# Acquisizione dati
E,   sE   = np.loadtxt('e.dat',usecols=(0,1),unpack=True)*1e+19
E_H, sE_H = np.loadtxt('e_h.dat',usecols=(0,1),unpack=True)*1e-14
H_K, sH_K = np.loadtxt('h_k.dat',usecols=(0,1),unpack=True)*1e+11
E_K, sE_K = np.loadtxt('e_k.dat',usecols=(0,1),unpack=True)*1e-4

#seleziono i migliori valori
e   = E
e_h = E_H[5]
h_k = H_K[2]
e_k = E_K[12]

se   = sE
se_h = sE_H[5]
sh_k = sH_K[2]
se_k = sE_K[12]
'''
print('e :', ce)
print('e/h :', ce/ch)
print('h/k :', ch/ck)
print('e/k :', ce/ck)

print("e:   ", e,   "+-", se)
print("e_h: ", e_h, "+-", se_h)
print("h_k: ", h_k, "+-", sh_k)
print("e_k: ", e_k, "+-", se_k)
'''
#par = [ce, ch, ck] #e, h, k
par = [1.6, 6.6, 1.36] #e, h, k
mis = [e, e_h, h_k, e_k]
err = [se, se_h, sh_k, se_k]
m = Minuit(fcn, par)
'''
m.limits[0] = (par[0]*0.1, par[0]*10)
m.limits[1] = (par[1]*0.1, par[1]*10)
m.limits[2] = (par[2]*0.1, par[2]*10)
'''
m.errordef = Minuit.LEAST_SQUARES
m.print_level = 0
m.migrad()

print("Valori Minimizzati")
print("e =", m.values[0], "+-", m.errors[0])
print("h =", m.values[1], "+-", m.errors[1])
print("k =", m.values[2], "+-", m.errors[2])
print("CHI2 =", m.fval, m.valid)

print("Matrice di Covarianza")
print(m.covariance)
print(m.accurate)

# Calcolo e disegno delle regioni di confidenza
plt.figure(figsize=(18, 6))

# Disegno dei contour plots
plt.subplot(1, 3, 1)
m.draw_mncontour('x0', 'x1', cl=[1])
plt.title("Regione di confidenza 68% (e, h)")

plt.subplot(1, 3, 2)
m.draw_mncontour('x1', 'x2', cl=[1])
plt.title("Regione di confidenza 68% (h, k)")

plt.subplot(1, 3, 3)
m.draw_mncontour('x0', 'x1', cl=[1])
plt.title("Regione di confidenza 68% (e, k)")

plt.tight_layout()
m.draw_mnmatrix(cl = [1,2,3])
plt.show()

