#!/usr/bin/python
    
import sys,serial
from dmm import *
from ps  import *

#Pilotaggio power supply
#Inizializzazione
instr = psinit("USB0::0x0AAD::0x0135::035375056::INSTR")
#Selezione canale 1
pssel(instr,1)
#Erogazione di 12 V
valV = 12
cmd  = f'APPLY {valV},0.1'
instr.write(cmd)

#File di output
file = open('out.dat','w')
#Configurazione seriale
ser = serial.Serial('COM2', 9600)
#Lettura dal multimetro
V,eV = dmmread(ser)
print(V,eV)
file.write(str(V)+'\t')
file.write(str(eV)+'\t')
file.write('\n')
