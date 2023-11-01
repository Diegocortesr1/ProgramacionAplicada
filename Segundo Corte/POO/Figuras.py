import math
class Circul:
    def __init__(self,radio):
        self.radio = radio

    def calculararea(self):
        a = math.pi * math.pow(self.radio, 2)
        print("El area del circulo es:", a)
    def calcularperimetro(self):
        p = 2* math.pi * self.radio
        print("El perimetro del circulo es:", p)

class cuadrado:
    def __init__(self,lado):
        self.lado = lado

    def calculararea(self):
        a = self.lado * self.lado
        print("El area del cuadrado es:", a)
    def calcularperimetro(self):
        p = 4 *self.lado
        print("El perimetro del cuadrado es:", p)

class rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base 
  
    def calculararea(self):
        a = self.altura * self.base
        print("El area del rectangulo es:", a)
    def calcularperimetro(self):
        p = 4 * (self.altura + self.base)
        print("El perimetro del rentangulo es:", p)

class Triangulo_rectangulo:
    def __init__(self,CatetoOpuesto,CatetoAdyacente,Hipotenusa):
        self.CatetoOpuesto = CatetoOpuesto
        self.CatetoAdyacente = CatetoAdyacente
        self.Hipotenusa = Hipotenusa
  
    def calculararea(self):
        a = (self.CatetoOpuesto*self.CatetoAdyacente)/2
        print("El area del triangulo es:", a)
    def calcularperimetro(self):
        p = 4 * (self.CatetoAdyacente + self.CatetoOpuesto + self.Hipotenusa)
        print("El perimetro del triangulo es:", p)




print("\nBienvenido al programa que calcula areas y perimetros")
print ("Desea calcular el area y el preimetro de una figura nueva? (Si/No)")
c = input("---->")

while True:
 while (c == "Si"):
   print("\nSeleccione cual figura desea calcular el area y perimetro desea calcular ")
   print("1. Circulo"+"\n"+"2. Cuadrado"+"\n"+"3. Rectangulo"+"\n"+"4. Triangulo rectangulo"+ "\n")
   s= int(input("---->"))

   if (s == 1, 2, 3, 4):  
    
     if (s == 1):
      r= int(input("\ningrese el radio del circulo:"+"\n"+"---->"))
      print(" ")
      Circulo = Circul(r)
      Circulo.calculararea() 
      Circulo.calcularperimetro()
      s = 1
      c = "Si"
      print ("\n")
      break
     
     if (s == 2):
      l= int(input("\ningrese el lado del del cuadrado:"+"\n"+"---->"))
      print(" ")
      Cuadrado = cuadrado(l)
      Cuadrado.calculararea()
      Cuadrado.calcularperimetro()
      print ("\n")
      s = 1
      c = "Si"
      break
     
     if (s== 3):
      b =int(input("\ningrese la base del rectangulo:"+"\n"+"---->"))
      a =int(input("ingrese la altura del rectangulo:"+"\n"+"---->"))
      print(" ")
      Rectangulo = rectangulo(a,b)
      Rectangulo.calculararea()
      Rectangulo.calcularperimetro()
      print ("\n")
      s = 1
      c = "Si"
      break
     
     if (s== 4):
      CO = int(input("\ningrese el cateto opuesto del triangulo:"+"\n"+"---->"))
      CA = int(input("ingrese la cateto adyacente del triangulo:"+"\n"+"---->"))
      H =  int(input("ingrese la hipotenusa:"+"\n"+"---->"))
      print(" ")
      Triangulo = Triangulo_rectangulo(CO,CA,H)
      Triangulo.calculararea()
      Triangulo.calcularperimetro()
      print ("\n")
      s = 1
      c = "Si"
      break   
   if (s != 1,2,3,4):
      print ("OPCION NO VALIDA\n")
      s = 1
      c = "Si"
      break
 
 while (c == "No"):
   print ("\nDe acuerdo, hasta luego\n")
   exit()
   

 if (c != ("Si")):
    if (c != ("No")):
     print ("OPCION NO VALIDA\n")
    

 print ("Desea calcular el area y el preimetro de una figura nueva? (Si/No)")
 c = input("---->")   







