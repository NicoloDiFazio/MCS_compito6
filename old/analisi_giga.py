import ROOT
import numpy as np

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

files = [file5]
#'''
for line in file1:
    str = line.split()
    if len(str)>0:
        V = np.append(V,float(str[0]))
        eV = np.append(eV, 0)
        T = np.append(T,float(str[1])+273.15)
        eT = np.append(eT,0.24089950000000002/abs(A*R0))
        I = np.append(I,float(str[2]))
        eI = np.append(eI,float(str[3]))
#'''     
for file in files:
    for line in file:
        str = line.split()
        if len(str)>0:
            V = np.append(V,float(str[0]))
            eV = np.append(eV, 0)
            R = np.append(R,float(str[1]))
            eR = np.append(eR,float(str[2]))
            I = np.append(I,float(str[3]))
            eI = np.append(eI,float(str[4]))
            
            T = np.append(T,(float(str[1])/R0 - 1)/A + 273.15)
            eT = np.append(eT,float(str[2])/abs(A*R0))
#'''
for i in range (0, len(I)):
    V_T  = np.append(V_T, V[i]/T[i])
    eV_T = np.append(eV_T, V_T[i]*eT[i]/T[i])
    
gr = ROOT.TGraphErrors(len(V_T), V_T, I, eV_T, eI)

f = ROOT.TF1("f", "[0]*(exp([1]*x)-1)", V_T[0], V_T[len(V_T)-1])

f.SetParameter(0, 1e-09)
f.SetParameter(1, 1.16e4)

gr.Draw("AP")
gr.Fit("f")
print("e/k misurata: %f +- %f" %(f.GetParameter(1), f.GetParError(1)))
print("e/k real: ", 1.6e-19/1.38e-23)
f.Draw("SAME")
ROOT.gApplication.Run(True)
