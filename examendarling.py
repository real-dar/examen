import os
os.system("cls")




productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
#stock = {modelo: [precio, stock]}
stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def stock_marca():
    os.system("cls")
    marca = int(input("Ingrese Marca a Consultar: "))
    
    marcas_disponibles = set()
    print("1. Stock marca")
    print(f"Marca disponible:", {marcas_disponibles})
    marcas_disponibles = {productos[0]}
    #if marca in productos:


   
    
    pass
def busqueda_precio():
    os.system("cls")
    print("2. Búsqueda por precio")
    p_minimo = int(input("Ingrese precio mínimo: "))
    p_maximo = int(input("Ingrese precio máximo: "))
    try: 
        if p_minimo < 240000 or p_minimo >900000:
            print("No hay notebooks en ese rango de precios")
        elif p_minimo > 240000 and p_maximo <350000:
            print(f"Los notebooks entre los precios consultas son:", '123FHD', ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'] )
            
    except ValueError:
        print("Ingrese valores Enteros")
        return
    for producto in productos:
        for stoks in stock:

            pass



def actualizar_precio():
    marca= print(int(input("ingrese modelo a actualizar: ")))
    nuevo_precio = print(int(input("Ingrese nuevo precio")))
    notebok = False
    for stocks in stock:
        if stocks == marca:
            notebok = True
            stocks[stocks][0] += nuevo_precio
        else:
            pass    



def menu():
    
    print("**** MENU PRINCIPAL ****")
    print("1. Stock marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
            
    while True:            
            opcion = int(input("ingrese opción a consultar: "))
            try:
                if opcion >1 and opcion <4:
                    pass
                else:
                    print("Ingrese una de las opciones disponibles")
            except ValueError:
                    print("ingrese un numero entero")

            if opcion ==1:
                stock_marca()
                
            elif opcion == 2:
                busqueda_precio()
                
            elif opcion == 3:
                actualizar_precio()

            elif opcion == 4:
                print("Programa Finalizado")
            else:
                print("Ingrese opciones disponibles")




menu()










