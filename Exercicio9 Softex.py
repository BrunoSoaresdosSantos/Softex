from configparser import Interpolation
import time


i = int(input("Quantos segundos para a Bomba explodir? "))

print("Começando a contagem")
for i in range(i, -1 , -1):
    print(i)
    time.sleep(1)
    if(i==0):
        print("BUUUUUUM!")