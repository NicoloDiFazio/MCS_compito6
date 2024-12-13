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

files = [file1, file2, file3, file4, file5]
#file Temperatura ambiente
for line in file1:
    str = line.split()
    if len(str)>0:
        V = np.append(V,float(str[0]))
        eV = np.append(eV, 2e-3)
        R = np.append(R, 0)
        eR = np.append(eR, 0)
        T = np.append(T,float(str[1])+273.15)
        eT = np.append(eT,0.24089950000000002/abs(A*R0))
        I = np.append(I,float(str[2]))
        eI = np.append(eI,float(str[3]))

for i in range (0, n+1):
    V_T  = np.append(V_T, V[i]/T[i])
    eV_T = np.append(eV_T, V_T[i]*m.sqrt((eV[i]/V[i])**2+(eT[i]/T[i])**2))
    #eV_T = np.append(eV_T, V_T[i]*eT[i]/T[i])

#file Temperatura fredda 1
for file in files:
    for line in file2:
        str = line.split()
        if len(str)>0:
            V = np.append(V,float(str[0]))
            eV = np.append(eV, 2e-3)
            R = np.append(R,float(str[1]))
            eR = np.append(eR,float(str[2]))
            T = np.append(T,(float(str[1])/R0 - 1)/A + 273.15)
            eT = np.append(eT,float(str[2])/abs(A*R0))
            I = np.append(I,float(str[3]))
            eI = np.append(eI,float(str[4]))
            
    for i in range (0, n+1):
        V_T  = np.append(V_T, V[i]/T[i])
        eV_T = np.append(eV_T, V_T[i]*m.sqrt((eV[i]/V[i])**2+(eT[i]/T[i])**2))

V_Tamb = []
Iamb = []
eV_Tamb = []
eIamb = []

V_Tf1 = []
If1 = []
eV_Tf1 = []
eIf1 = []

V_Tf2 = []
If2 = []
eV_Tf2 = []
eIf2 = []

V_Tc1 = []
Ic1 = []
eV_Tc1 = []
eIc1 = []

V_Tc2 = []
Ic2 = []
eV_Tc2 = []
eIc2 = []

for i in range(0, n+1):
    V_Tamb.append(V_T[i])
    Iamb.append(I[i])
    eV_Tamb.append(eV_T[i])
    eIamb.append(eI[i])
    
for i in range(n+1, 2*n+1):
    V_Tf1.append(V_T[i])
    If1.append(I[i])
    eV_Tf1.append(eV_T[i])
    eIf1.append(eI[i])

for i in range(2*n+1, 3*n+1):
    V_Tf2.append(V_T[i])
    If2.append(I[i])
    eV_Tf2.append(eV_T[i])
    eIf2.append(eI[i])
    
for i in range(3*n+1, 4*n+1):
    V_Tc1.append(V_T[i])
    Ic1.append(I[i])
    eV_Tc1.append(eV_T[i])
    eIc1.append(eI[i])
    
for i in range(4*n+1, 5*n+1):
    V_Tc2.append(V_T[i])
    Ic2.append(I[i])
    eV_Tc2.append(eV_T[i])
    eIc2.append(eI[i])
    
gramb = ROOT.TGraphErrors(len(V_Tamb), V_Tamb, Iamb, eV_Tamb, eIamb)
famb = ROOT.TF1("f", "[0]*(exp([1]*x)-1)", V_Tamb[0], V_Tamb[len(V_Tamb)])
famb.SetParameter(0, 1e-09)
famb.SetParameter(1, 1.16e4)

gramb.Draw("AP")
gramb.Fit("f")
print("e/k misurata: %f +- %f" %(famb.GetParameter(1), famb.GetParError(1)))
print("e/k real: ", 1.6e-19/1.38e-23)
famb.Draw("SAME")
ROOT.gApplication.Run(True)
