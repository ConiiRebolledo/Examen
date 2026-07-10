#SalaCineMax

peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def leer_opcion():
    try:
        while True:
            op = int(input("Ingrese una opcion (1-6): "))
            return op
    except ValueError:
        return -1       

def cupos_genero(genero, peliculas, cartelera):
    resultados = []
    for codigo, lista_datos in peliculas.items():
        if genero == lista_datos[1] and cartelera[codigo][1] > 0:
            resultados.append(f"{lista_datos[1]}--{codigo}")
    resultados.sort()
    return resultados

def busqueda_precio(p_min, p_max,):
    try:
        resultados=[]
        for codigo, datos in peliculas.items():
            precio=cartelera[codigo][0]
            if p_min <= precio <= p_max > 0:
                resultados.append(f"{datos[0]} --- {precio}")
        resultados.sort()
        return resultados
    except ValueError:
        print("Ingrese numeros")

def buscar_codigo(peliculas, codigo):
    return codigo in peliculas

def actualizar_precio(codigo, nuevo_valor, cartelera):
    if codigo in cartelera:
        cartelera[codigo][0] = nuevo_valor
        return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(peliculas, codigo):
        return False
    else:
        peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
        cartelera[codigo] = [precio, cupos]
        return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    if buscar_codigo(peliculas,codigo):
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    return False

def main():
    
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        op = leer_opcion()
        
        if op==1:
            resultados_genero = input("Ingrese genero a consultar: ").lower()
            CuposGenero = cupos_genero(resultados_genero, peliculas, cartelera)
            if len(CuposGenero)>0:
                for i in cupos_genero:
                    print (f"El total de cupos disponibles es: {i}")
            else:
                print("No hay coincidencias con el genero")
                
        if op==2: 
            try:
                p_min = int(input("Ingrese el precio minimo de la pelicula"))
                p_max = int(input("Ingrese el precio maximo de la pelicula"))
                if p_min < 0:
                    print("Ingrese un precio mayor a cero")
                    return p_min
                resultados = busqueda_precio(p_min, p_max)
                if resultados:
                    print ("Las peliculas encontradas son: ")
                    for resultado in resultados:
                        print(resultado)
                else:
                    print("No se encontraron peliculas en ese rango de precio")
            except ValueError:
                print("Ingrese numeros")
                
        if op==3:
            while True:
                codigo = input("Ingrese el codigo de la pelicula")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio de la pelicula"))
                    exito = actualizar_precio(codigo, nuevo_precio, cartelera)
                    if exito:
                        print("Precio Actualizado!")
                    else:
                        print("El codigo no existe!")
                    confirmar = input("¿Desea actualizar otro precio (s/n)").lower()
                    if confirmar == "n":
                        break
                except ValueError:
                    print("Debe ingresar numeros enteros")
                    
        if op==4:
            codigo = input("Ingrese un nuevo codigo").strip()
            if buscar_codigo(peliculas, codigo):
                print("El codigo ya existe")
            else:
                titulo = input("Ingrese el Titulo de la pelicula").strip()
                if titulo:
                    print()
                else:
                    print("El codigo no puede estar vacio ni contener espacios")
                
                genero = input("Ingrese el genero de la pelicula").strip()
                if genero:
                    print()
                else:
                    print("El codigo no puede estar vacio ni contener espacios")
                
                clasificacion = input("Ingrese la clasificacion de la pelicula")
                if clasificacion == "A" or "B" or "C":
                    print()
                else:
                    print("Ingrese las letras A, B o C de clasificación")
                    
                idioma = input("Ingrese el idioma de la pelicula").strip()
                if idioma:
                    print()
                else:
                    print("El codigo no puede estar vacio ni contener espacios")
                    
                es_3d = input("Ingrese si la pelicula es 3d (s/n)")
                if es_3d=="n" or es_3d=="s":
                    print()
                else:
                    print("Ingrese (s) si es 3d y (n) si no es 3d")
                    
                try:
                    duracion = int(input("Ingrese la duracion de la pelicula")).strip()
                    if duracion > 0:
                        print()
                    else:
                        print("Ingrese un numero entero mayor que cero")
                    precio=int(input("Ingrese el precio de la pelicula"))
                    if precio > 0:
                        print()
                    else:
                        print("Ingrese un numero entero mayor que cero")
                    cupos=int(input("Ingrese la cantidad de cupos para la pelicula"))
                    if cupos >= 0:
                        print()
                    else:
                        print("Ingrese un numero entero mayor o igual a cero")
                except ValueError:
                    print("Ingrese numeros")
                    
        if op == 5:
            codigo = input("Ingrese el codigo de pelicula a eliminar")
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Eliminada")
            else:
                print("El codigo no existe")
                
        if op==6:
            print("Programa finalizado")
            break
        else:
            print("Opcion Invalida")
                
main()               