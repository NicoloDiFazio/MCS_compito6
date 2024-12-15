import ROOT as R
import math as m
import numpy as np

#par =[6.7,1.6,0.30,0.28,0.35] #parametro di normalizzazione, media, sigma, Ampiezza1, Ampiezza2
p = 6.78
a1 = 0.28
mu1 = 1.67
sig1 = 0.19
a2 = 0.34
mu2 = 3.13
sig2 = 0.29
a3 = 0.38
mu3 = 4.76
sig3 = 0.39

par =[p, a1,mu1,sig1, a2,mu2,sig2, a3,mu3,sig3] #parametro di normalizzazione, Ampiezza1, media1, sigma1, Ampiezza2, media2, sigma2, Ampiezza3 media3, sigma3
pars =['p', 'a1','mu1','sig1', 'a2','mu2','sig2', 'a3','mu3','sig3']
#definisco funzione multigaussiana
def multiGauss(x, par):
    # Funzione multi-gaussiana: somma di 3 gaussiane
    # par contiene: [A1, mu1, sigma1, A2, mu2, sigma2, A3, mu3, sigma3]
    return par[0]*(par[1] * R.TMath.Gaus(x[0], par[2], par[3], 1) +
                   par[4] * R.TMath.Gaus(x[0], par[5], par[6], 1) +
                   par[7] * R.TMath.Gaus(x[0], par[8], par[9], 1))

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

e = np.array([f.GetParameter(5)-f.GetParameter(2), f.GetParameter(8)-f.GetParameter(5)])

print("e = %f +- %f" %(e.mean(), e.var()))
R.gApplication.Run(True)

