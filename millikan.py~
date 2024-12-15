import ROOT as R
import math as m
import numpy as np

par =[6.7,1.6,0.30,0.28,0.35] #parametro di normalizzazione, media, sigma, Ampiezza1, Ampiezza2
#definisco funzione multigaussiana
def multiGauss(x, par):
    # Funzione multi-gaussiana: somma di 3 gaussiane
    # par contiene: [A1, mu1, sigma1, A2, mu2, sigma2, A3, mu3, sigma3]
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
f = R.TF1("f", multiGauss, 0, 5.5, 5)
for i in range (5):
    f.SetParameter(i, par[i])
    
a.Draw()
a.Fit("f","LR")

for i in range (5):
    print("parametro", i,":", f.GetParameter(i))
    
R.gApplication.Run(True)

