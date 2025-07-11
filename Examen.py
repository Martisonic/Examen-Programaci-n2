#productos = {'modelo': ['marca', 'pantalla', 'RAM', 'disco', 'GB de DD', 'procesador', 'video', 'model'],}


productos = {
             '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050', '8475HD'],
             '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050', '2175HD'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti', 'JjfFHD'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada', 'fgdxFHD'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050', 'GF75HD'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada', '123FHD'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050', '342FHD'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050', 'UWU131HD'], 
}

#stock = {'modelo': ['precio', 'stock'],}

stock = {
    '8475HD': [387990,10, 'HP'],
    '2175HD': [327990,4, 'Lenovo'], 
    'JjfFHD': [424990,1, 'Asus'],
    'fgdxFHD': [664990,21, 'HP'], 
    '123FHD': [290890,32, 'Asus'], 
    '342FHD': [444990,7, 'Lenovo'],
    'GF75HD': [749990,2, 'Lenovo'], 
    'UWU131HD': [349990,1, 'Dell'], 
    'FS1230HD': [249990,0, 'Dell'], 
}

def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if(datos[0].lower() == marca.lower()):
            total += stock[codigo][1]
    print (f"El stock total para '{marca}' es: {total}")

def búsqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos [0]
        if(precio >= p_min and precio <= p_max) and (stock[codigo][1] > 0):
           resultados.append(datos[2] + '--' + codigo)
    if resultados:
        resultados.sort()
        print("Productos encontrados:", resultados)
    else:
        print("No hay productos en ese rango de precio")

def actualizar_precio(modelo, p):
    if(modelo in productos):
        stock[modelo][0] = p
        return True
    return False

def main():
    while True:

        print ("*** MENU PRINCIPAL ***")
        print ("1. Stock marca.")
        print ("2. Búsqueda por precio.")
        print ("3. Actualizar precio.")
        print ("4. Salir.")

        opcion = int(input("Seleccione una de las opciones disponibles del 1 al 4 = "))

        if opcion == 1:
           marca = input("Ingrese la marca que busca (HP/Lenovo/Asus/Dell) = ")
           stock_marca(marca)

        elif opcion == 2:
            try:
                p_min = float(input("Ingrese un precio minimo = "))
                p_max = float(input("Ingrese un precio maximo = "))
                búsqueda_precio(p_min, p_max)
            except ValueError:
                print ("Debe ingresar numeros enteros, vuelva a intentar")

        elif opcion == 3:
            while True:
                modelo = (input("Ingrese codigo de producto: "))
                try:
                    p = int(input("Ingrese nuevo precio = "))
                    if actualizar_precio(modelo, p):
                        print ("Precio actualizado")
                    else:
                        print("El codigo no existe")
                except ValueError:
                    print("Debe ingresar un numero entero para el precio, vuelva a intentar")

                repetir = input("Desea actualizar el precio a otro producto (s/n)? = ").lower()
                if repetir != 's':
                    break
        elif opcion == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opcion valida (1, 2, 3 o 4)")

if __name__ == "__main__":
    main()