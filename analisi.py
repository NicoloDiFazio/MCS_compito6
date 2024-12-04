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

file = open('out.dat','r')

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
        #print(T)

for i in range (0, n+1):
    V_T  = np.append(V_T, V[i]/T[i])
    
gr = ROOT.TGraphErrors(len(V_T),V_T,I,eV,eI)


f = ROOT.TF1("f", "[0]*(exp([1]*x)-1)", min, max)

f.SetParameter(0, 1e-09)
f.SetParameter(1, 1.16e4)

gr.Draw("AP")
gr.Fit("f")
print(f.GetParameter(1), f.GetParError(1))
print("e/k ",1.6e-19/1.38e-23)
f.Draw("SAME")
ROOT.gApplication.Run(True)
