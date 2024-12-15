import ROOT
import numpy as np
import math as m

min = 0.3
max = 0.5
n = 20

R0 = 100  #resist a 0 C
A = 3.9e-3 #costante

V  = np.array([])
eV = np.array([])
R  = np.array([])
eR = np.array([])
I  = np.array([])
eI = np.array([])
T  = np.array([])
eT = np.array([])
V_T  = np.array([])
eV_T  = np.array([])

file1 = open('outBuonoSiTemp.dat','r')
file2 = open('outFreddo.dat','r')
file3 = open('outFreddo2.dat','r')
file4 = open('outCaldo.dat','r')
file5 = open('outCaldo2.dat','r')

files = [file2, file3, file4, file5]
colors = [4, 4, 2, 2]
GR = []

k = 0
gr = ROOT.TGraphErrors()

#file Temperatura ambiente
for line in file1:
    str = line.split()
    if len(str)>0:
        V = float(str[0])
        eV = 2e-3
        R = 0
        eR = 0
        T = float(str[1]) + 273.15
        eT = 0.24089950000000002/abs(A*R0)
        I = float(str[2])
        eI = float(str[3])
        x = V/T
        ex = x*np.sqrt((eT/T)**2 + (eV/V)**2)

        gr.SetPoint(k, x, I)
        gr.SetPointError(k, ex, eI)

        k+=1
GR.append(gr)

#file temperature diverse

i = 0
for file in files:
    k = 0
    gr = ROOT.TGraphErrors()    
    for line in file:
        str = line.split()
        if len(str)>0:
            V = float(str[0])
            eV = 2e-3
            R = float(str[1])
            eR = float(str[2])
            T = (R/R0 - 1)/A + 273.15
            eT = eR/abs(A*R0)
            I = float(str[3])
            eI = float(str[4])
            x = V/T
            ex = x*np.sqrt((eT/T)**2 + (eV/V)**2)
            
            gr.SetPoint(k, x, I)
            gr.SetPointError(k, ex, eI)

            k+=1
    gr.SetMarkerStyle(20)
    gr.SetMarkerSize(0.5)
    gr.SetMarkerColor(colors[i])
    GR.append(gr)
    i+=1

GR[0].Draw("AP")
for j in range (1, len(GR)):
    GR[j].Draw("P")

f = ROOT.TF1("f", "[0]*(exp([1]*x)-1)", 0, 0.1)
f.SetParameter(0, 1e-15)
f.SetParameter(1, 1.16e4)

temperatura = ['Ambiente', 'Fredda 1', 'Fredda 2', 'Calda 1', 'Calda 2']

for j in range (len(GR)):
    GR[j].Fit("f")
    print("e/k misurata a temperatura", temperatura[j], ": %f +- %f" %(f.GetParameter(1), f.GetParError(1)))
    print("e/k real: ", 1.6e-19/1.38e-23)

ROOT.gApplication.Run(True)
