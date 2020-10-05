ruta = ""
direccion = ""
contador_autores = 1
oraciones = []

class Oracion:
    def __init__(self, autor, nota):
        self.autor = autor
        self.nota = nota

    def __str__(self):
        return str(self.__dict__)

def menu():
    print("***************************************************************")
    print("Menu: ")
    print("\t1. Ingresa ruta.")
    print("\t2. Ingresa dirección.")
    print("\t3. Ver datos.")
    print("\t4. Enviar datos.")
    print("\t5. Salir")
    print("***************************************************************")
    print("")

def crear_objetos(texto):
    global contador_autores
    global oraciones
    del oraciones
    contador_autores = 1

    arreglo = texto.split(".")
    for oracion in arreglo:
        oraciones.append(Oracion("Autor#"+str(contador_autores),oracion))
        contador_autores += 1
    
def ver_datos():
    global oraciones

    for oracion in oraciones:
        print(oracion)

while True: 
    menu()
    opcion = int(input("Escoje una opción: "))

    if opcion == 1:
        ruta = input("Dirección del archivo: ")
        f = open(ruta)
        crear_objetos(f.read())
        print("Datos ingresados!")
        print("")
    
    elif opcion == 2:
        direccion = input("Dirección del balanceador: ")
        print("Direccion Ingresada!")
        print("")
    
    elif opcion == 3:
        ver_datos()
    
    elif opcion == 4:
        print("Datos Enviados!")

    elif opcion == 5:
        print("Vuelve pronto!")
        break