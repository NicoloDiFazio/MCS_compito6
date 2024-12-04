#!/usr/bin/python
import sys, serial
from dmm import *
ser = serial.Serial("COM5", 9600)
R, eR = dmmread(ser)

print(R, eR)

R0 = 100
A = 3.9e-3

T = (R/R0 - 1)/A

print(T)
