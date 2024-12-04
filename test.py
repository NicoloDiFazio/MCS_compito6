#!/usr/bin/python
    
import sys,serial
from dmm import *
from ps  import *
import time

#Misura resistenza x temperatura
serT = serial.Serial("COM5", 9600)

#Pilotaggio power supply
#Inizializzazione
gen = 'USB0::0x0AAD::0x0135::035375051::INSTR'
instr = psinit(gen)
#Selezione canale 1
pssel(instr,1)

#Configurazione seriale
ser = serial.Serial('COM4', 9600)

#File di output
file = open('out.dat','w')

min = 0.3    #roba per ciclo con dati min e max del V
max = 0.5
n = 20
passo = (max-min)/n

R0 = 100  #resist a 0 C
A = 3.9e-3 #costante

for i in range (0,n+1):   #ciclo variazione V e stampa su file
    #Erogazione di Voltaggio
    V = min + (i*passo)
    cmd  = f'APPLY {V},0.1'
    instr.write(cmd)

    time.sleep(1)

    #Lettura dal multimetro
    I,eI = dmmread(ser)
    R, eR = dmmread(serT) #temp
    print(V, R, eR, I, eI)
    file.write(str(V)+'\t') #spazio
    file.write(str(R)+'\t') #spazio
    file.write(str(eR)+'\t') #spazio
    file.write(str(I)+'\t') #spazio
    file.write(str(eI)+'\t') #spazio
    file.write('\n') #a capo

