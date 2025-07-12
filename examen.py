import os
os.system
productos = {'8475HD': ['HP', 15.6, '8GB', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],           
            }
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1]
}

def menu():
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")
menu()    