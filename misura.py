import ROOT
import numpy as np
import math as m

e = np.array([])
e_h = np.array([])
h_k = np.array([])
e_k = np.array([])

file1 = open('e.dat','r')
file2 = open('e_h.dat','r')
file3 = open('h_k.dat','r')
file4 = open('e_k.dat','r')

files = [file1, file2, file3, file4]

i = 0
for file in files:   
    for line in file:
        str = line.split()
        if len(str)>0:
            if i = 0:
                e = np.append(e, float(str[0]))
            if i = 1:
                e = np.append(e, float(str[0]))
            if i = 2:
                e = np.append(e, float(str[0]))
            if i = 3:
                e = np.append(e, float(str[0]))
    i += 1
