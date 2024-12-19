import ROOT as R
import math as m
import numpy as np

#par =[6.7,1.6,0.30,0.28,0.35] #parametro di normalizzazione, media, sigma, Ampiezza1, Ampiezza2
p = 6.7
mu = 1.6
sig = 0.30
a1 = 0.28
a2 = 0.35

par =[p,mu,sig,a1,a2] #parametro di normalizzazione, media, sigma, Ampiezza1, Ampiezza2
pars =['p','mu','sig','a1','a2']
#definisco funzione multigaussiana
def multiGauss(x, par):
    # Funzione multi-gaussiana: somma di 3 gaussiane
    return par[0]*(par[3] * R.TMath.Gaus(x[0], par[1], par[2], 1) +
                   par[4] * R.TMath.Gaus(x[0], 2*par[1], par[2], 1) +
                   (1-par[4]-par[3]) * R.TMath.Gaus(x[0], 3*par[1], par[2], 1))

dat=[]

#apertura file
file = open('Millikan.dat','r')

for line in file:
    dat.append(float(line.strip()))

#istogramma
a = R.TH1D("a", "Istogramma", 100, 0,10)  #dato min e max
for value in dat:
    a.Fill(value) # Riempio istogramma con i dati

#fit
f = R.TF1("f", multiGauss, 0, 5.5, len(par))
for i in range (len(par)):
    f.SetParameter(i, par[i])
    
a.Draw()
a.Fit("f","LR")

for i in range (len(par)):
    print(pars[i],":", par[i])
    print(pars[i],"fit:", f.GetParameter(i))

print("e = %f +- %f" %(f.GetParameter(1), f.GetParError(1)))
R.gApplication.Run(True)

