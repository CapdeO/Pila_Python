"""globales"""
cima = -1
pila_llena = False
pila_vacia = False
cant_elem = 0
maximo = 0
p = []

def llena ():
  global pila_llena
  if maximo == cima + 1:
    pila_llena = True
    
  else:
    pila_llena = False
    

def vacia():
  global pila_vacia
  if cima == -1:
    pila_vacia = True
    
  else:
    pila_vacia = False
    

def crear_pila():
  global p
  p = []
  global maximo
  maximo = int(input("ingrese un máximo: "))
  global cima
  cima = -1

def cantidad():
  global cant_elem
  cant_elem = cima + 1

def apilar():
  llena()
  if pila_llena == True:
    print("La pila está llena")
  else:
    ingreso = int(input("Ingrese número: "))
    p.append(ingreso)
    global cima
    cima = cima + 1
    print("La pila es: ", p)
    global cant_elem
    cant_elem = cant_elem + 1
    

def desapilar():
  vacia()

  
  if pila_vacia == True:
    print("Pila vacía")
  else:
    global cima
    p.pop(cima)
    cima = cima - 1
    global cant_elem
    cant_elem = cant_elem - 1


print("¿Qué quieres hacer? \n1) Crear pila\n2) Apilar\n3) Desapilar\n4) Saber si está llena\n5) Saber si está vacía\n6) Saber la cantidad de elementos\n7) Salir")
corte = int(input("Elija una opción:"))
while corte != 7:
  
  if corte == 1:
    crear_pila()
    print("Pila creada")
    print("El maximo es: ", maximo)
    print("La cima es: ", cima)
  elif corte == 2:
    apilar()
  elif corte == 3:
    desapilar()
  elif corte == 4:
    llena()
    if pila_llena == True:
      print("La pila está llena")
    else:
      print("La pila no está llena")
  elif corte == 5:
    vacia()
    if pila_vacia == True:
      print("La pila está vacía")
    else:
      print("La pila no está vacía")
  elif corte == 6:
    print("La cantidad de elementos es: ", cant_elem)
  
    
  
  
  corte = int(input("Elija una opción:"))
