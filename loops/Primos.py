import time
inicio = time.time()




for x in range(0,31):
    contar = 0
    for n in range(1, x+1):
        residue = x%n
        if residue == 0:
            contar = contar + 1
              
    if contar == 2:
        print(f'{x} es un primo')
        
fin = time.time()
print("t = ", (fin - inicio)*1000)