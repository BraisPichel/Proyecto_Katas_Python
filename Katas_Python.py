1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
	
def contar_letras(cadena_texto):
    frecuencia = {} 

    for letra in cadena_texto:  
        if letra != " ":  
            if letra in frecuencia:
                frecuencia[letra] += 1  
            else:
                frecuencia[letra] = 1  

    return frecuencia  

#Ejemplo:
print(contar_letras("Hola Python"))  

#Output esperado:
#{'H': 1, 'o': 2, 'l': 1, 'a': 1, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}


2.Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()


lista = [1,2,3,4,5]
 
lista_doble_valor = list(map(lambda x: x * 2 , lista))


print(lista_doble_valor)

#Output esperado:
#[2,4,6,8,10]


3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista, objetivo):
    return [palabra for palabra in lista if objetivo in palabra]

#Ejemplo:
palabras = ["coche","mascota","padre","casa","patinete","profesor","pantera"]

print(buscar_palabras(palabras, "pa"))

#Output esperado:
#['padre', 'patinete', 'pantera']


4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1,lista2):

    return list(map(lambda x, y : x - y , lista1, lista2))

lista1 = [8,5,7,9,13]
lista2 = [1,2,3,4,5]

resultado = diferencia_listas(lista1,lista2)

print(resultado)

#Output esperado:
#[7,3,4,5,8]


5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado. 

def calcular_estado(lista_numeros,nota_aprobado=5):
    if not lista_numeros:
        return (0,"suspenso")
    

    media = sum(lista_numeros) / len(lista_numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"

    return (media,estado)

#Ejemplo:

notas = (5,3,8)
resultado = calcular_estado(notas)

print(resultado)

#Output esperado:
#(5.333333333333333, 'aprobado')


6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  
    
#Ejemplo:
print(factorial(4))

#Output esperado:
#24


7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(str, lista_tuplas))

#Ejemplo:

tuplas = [("Hola","Python"),(1,2,3)]

resultado = tuplas_a_strings(tuplas)
print(resultado)

#Output esperado:
#["('Hola', 'Python')", '(1, 2, 3)']


8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        
        numero1 = float(input("Ingresa el primer numero"))
        numero2 = float(input("Ingresa el segundo numero"))

        resultado = numero1 / numero2

        print(f"La division ha sido EXITOSA, por lo que {numero1} ÷ {numero2} = {resultado}")

    except ValueError:
        print("Hay un ERROR ya que se ha introducido un valor no numerico")

    except ZeroDivisionError:
        print("Hay un ERROR, ya que no se puede dividir entre cero")

dividir_numeros()


9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def mascotas_permitidas(lista_mascotas):
    mascotas_prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}  
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

#Ejemplo:

mascotas = ["Perro","Gato","Hamster","Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

resultado = mascotas_permitidas(mascotas)

print(resultado)

#Ouput esperado:
#['Perro', 'Gato', 'Hamster']


10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista):
    if not lista:  
        raise ValueError("La lista está vacía.")  
    return sum(lista) / len(lista) 

try:
    print(calcular_promedio([1, 2, 3])) 
    print(calcular_promedio([])) 
except ValueError as e:
    print(e) 

#Output esperado:
#2.0
#La lista está vacía.


11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.

def introduzca_edad():
     
    try:
        edad = int(input("Introduzca aquí su edad: "))
        if 0 <= edad <= 120:
            print(f"La edad {edad} es un valor válido.")
        else:
            print("La edad introducida debe estar entre 0 y 120.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

introduzca_edad()
      

12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    return list(map(len, frase.split()))

#Ejemplo

frase = "Estoy aprendiendo Python"

resultado = longitud_palabras(frase)

print(resultado)

#Output esperado:
#[5, 11, 6]


13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() 

def convertir_mayusculas_minusculas(cadena):
    return list(map(lambda letra: (letra.upper(), letra.lower()), sorted(set(cadena))))

print(convertir_mayusculas_minusculas("Estoy aprendiendo a programar en Python"))

#Output esperado:
#[(' ', ' '), ('E', 'e'), ('P', 'p'), ('A', 'a'), ('D', 'd'), ('E', 'e'), ('G', 'g'), ('H', 'h'), ('I', 'i'), ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'), ('R', 'r'), ('S', 's'), ('T', 't'), ('Y', 'y')]


14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_inicial(lista,letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista))

#Ejemplo:

resultado = filtrar_por_inicial(["casa","coche","llaves","perro"],"c")

print(resultado)

#Output esperado:
#['casa', 'coche']


15. Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [1,2,3,4,5]

resultado = list(map(lambda x: x + 3,numeros))

print(resultado)

#Output esperado:
#[4,5,6,7,8]


16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def filtrar_palabras_largas(texto, n):
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))

print(filtrar_palabras_largas("Estoy aprendiendo a programar en Python",6))

#Output esperado:
#['aprendiendo', 'programar']


17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
   return reduce(lambda x, y : x * 10 + y, digitos)

digitos = [5,7,2]

print(lista_a_numero([5,7,2]))

#Output esperado:
#572


18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [
    {"nombre": "María", "edad": 20, "calificacion": 70},
    {"nombre": "David", "edad": 24,"calificacion": 87},
    {"nombre": "Marta", "edad": 21, "calificacion": 93},
    {"nombre": "Pedro", "edad": 26, "calificacion": 97}
]

estudiantes_sobresalientes = list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

print(estudiantes_sobresalientes)

#Output esperado:
#[{'nombre': 'Marta', 'edad': 21, 'calificacion': 93}, {'nombre': 'Pedro', 'edad': 26, 'calificacion': 97}]


19.Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1,2,3,4,5]

numeros_impares = list(filter(lambda x: x % 2 != 0,numeros))

print(numeros_impares)

#Output esperado:
#[1,3,5]


20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar(lista):
    return list(filter(lambda x: isinstance(x,int),lista))

#Ejemplo:

lista1 = ["Hola",27,"Python",26,78]

resultado = filtrar(lista1)
print(resultado)

#Output esperado:
[27,26,78]


21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo_numero = lambda x: x ** 3

#Ejemplo:

print(cubo_numero(2))

#Output esperado:
#8


22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total_valores(lista_numeros):
    return reduce(lambda x, y : x * y , lista_numeros)

#Ejemplo:

lista1 = [1,2,3,4]

producto_total_valores(lista1)

#Output esperado:
#24


23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenacion_palabras(lista_palabras):
    return reduce(lambda x,y : x + " " + y,lista_palabras)

#Ejemplo:

lista_palabras = ["Estoy","aprendiendo","Python"]
resultado = concatenacion_palabras(lista_palabras)

print(resultado)

#Output esperado:
#Estoy aprendiendo Python


24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_valores_lista(lista_numeros):
    return reduce(lambda x, y : x - y , lista_numeros)

#Ejemplo:

lista1 = [70,3,25,13]

diferencia_valores_lista(lista1)

#Output esperado:
#29


25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_numero_caracteres(cadena):
    return len(cadena)

#Ejemplo:

frase = "Estoy aprendiendo Python"

resultado = contar_numero_caracteres(frase)
print(resultado)

#Output esperado:
#24


26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y : x % y

#Ejemplo:

print(resto_division(5,2))

#Output esperado:
#1


27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

#Ejemplo:

numeros = (4,6,8,10)

resultado = calcular_promedio(numeros)

print(resultado)

#Output esperado:
#7.0


28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    numeros_vistos = set()  

    for numero in lista:  
        if numero in numeros_vistos:  
            return numero
        numeros_vistos.add(numero)  

    return None

#Ejemplo:

lista1 = [1,2,3,4,5,6,7,8,9,2]

resultado = primer_duplicado(lista1)

print(resultado)  

#Output esperado:
#2

lista2 = [1, 2, 3, 4, 5]

resultado = primer_duplicado(lista2)

print(resultado)  

#Output esperado:
#None


29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro. 

def enmascarar_texto(texto):
    texto = str(texto)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

#Ejemplo:

print(enmascarar_texto("Hola Python")) 

#Output esperado:
########thon


30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def verificar_anagramas(palabra1,palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

#Ejemplo:

print(verificar_anagramas("Nepal", "panel"))

#Output esperado:
#True

print(verificar_anagramas("casa", "rata")) 

#Output esperado:
#False


31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción. 

def buscar_nombre():
    try:
        nombres= input("Ingresa una lista de nombres separados por comas").split(",")
        nombre = input("Ingresa el nombre a buscar").strip()

        if nombre in [n.strip() for n in nombres]:
            print(f"El nombre {nombre} esta en la lista")

        else:
            raise ValueError(f"El nombre {nombre} NO esta en la lista")

    except ValueError as e:
        print(e)

buscar_nombre()


32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre,empleados):
    for empleado in empleados:
        if empleado["nombre"] == nombre:
            return (f" El empleado {nombre} trabaja como {empleado['puesto']} en nuestra empresa")  
    return (f"El empleado {nombre} no trabaja en nuestra empresa")
                                

empleados = [
    {"nombre": "Marta Fernández", "puesto": "Directora comercial"},
    {"nombre": "Juan Pérez", "puesto": "Director de recursos humanos"},
    {"nombre": "Lola González", "puesto": "Gestora de producto"},
]                       

#Ejemplo:

print(buscar_empleado("Marta Fernández", empleados)) 

#Output esperado:
#El empleado Marta Fernández trabaja como Directora comercial en nuestra empresa

print(buscar_empleado("Carlos Rodríguez", empleados)) 

#Output esperado:
#El empleado Carlos Rodríguez no trabaja en nuestra empresa


33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_elementos_listas = lambda lista1, lista2: list(map(lambda x, y : x + y, lista1, lista2))

#Ejemplo:

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

resultado = sumar_elementos_listas(lista1,lista2)

print(resultado)

#Output esperado:
#[7,9,11,13,15]


34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.

Código a seguir:

1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas. 

Caso de uso: 

1. Crear un árbol. 
2. Hacer crecer el tronco del árbol una unidad. 
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad. 
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2. 
7. Obtener información sobre el árbol.

class Arbol:

    def __init__(self):

        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        self.tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self,posicion):
        
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
            
        else:
            print("Posicion no valida")

    def info_arbol(self):
        return (f" Arbol: tronco: {self.tronco}," 
                f" numero de ramas: {len(self.ramas)},"
                f" longitud de ramas: {self.ramas}")

#Caso de uso:

# 1. Crear un árbol.

Arbolito = Arbol()

# 2. Hacer crecer el tronco una unidad.

Arbolito.crecer_tronco()

# 3. Añadir una nueva rama al árbol.

Arbolito.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad.

Arbolito.crecer_ramas()

# 5.  Añadir dos nuevas ramas al árbol.

Arbolito.nueva_rama()
Arbolito.nueva_rama()

# 6. Retirar la rama situada en la posición 2.

Arbolito.quitar_rama(2)

# 7. Obtener informacion sobre el arbol:

print(Arbolito.info_arbol()) 

#Output esperado:
#class Arbol:

    def __init__(self):

        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        self.tronco += 1
    
    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self,posicion):
        
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
            
        else:
            print("Posicion no valida")

    def info_arbol(self):
        return (f" Arbol: tronco: {self.tronco}," 
                f" numero de ramas: {len(self.ramas)},"
                f" longitud de ramas: {self.ramas}")

#Caso de uso:

# 1. Crear un árbol.

Arbolito = Arbol()

# 2. Hacer crecer el tronco una unidad.

Arbolito.crecer_tronco()

# 3. Añadir una nueva rama al árbol.

Arbolito.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad.

Arbolito.crecer_ramas()

# 5.  Añadir dos nuevas ramas al árbol.

Arbolito.nueva_rama()
Arbolito.nueva_rama()

# 6. Retirar la rama situada en la posición 2.

Arbolito.quitar_rama(2)

# 7. Obtener informacion sobre el arbol:

print(Arbolito.info_arbol()) 

#Output esperado:
#Arbol: tronco: 2, numero de ramas: 2, longitud de ramas: [2, 1]


36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. 

Código a seguir: 

1.	Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False . 
2.	Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
3.	Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse. 
4.	Implementar el método agregar_dinero para agregar dinero al saldo del usuario. 

Caso de uso: 

1.	Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 
2.	Agregar 20 unidades de saldo de "Bob". 
3.	Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". 
4.	Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:

    def __init__(self,nombre,saldo,cuenta_corriente = True):
        self.nombre= nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self,cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} quiso retirar {cantidad} euros y no tiene suficiente saldo")
        self.saldo -= cantidad
        print(f"{self.nombre} retiro {cantidad} euros de su cuenta, por lo que su saldo actual es {self.saldo}")

    def transferir_dinero(self,otro_usuario,cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} quiso transferir {cantidad} euros, pero no tiene suficiente saldo")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print(f"{self.nombre} transfirio {cantidad} euros a {otro_usuario.nombre}, por lo que su saldo actual es {self.saldo}")
    
    def agregar_dinero(self,cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} agrego {cantidad} euros a su cuenta, por lo que su saldo actual es {self.saldo}")


#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.

alicia = UsuarioBanco("Alicia",100)
bob = UsuarioBanco("Bob",50)

#2.Agregar 20 unidades de saldo de "Bob".

bob.agregar_dinero(20)

#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".

bob.transferir_dinero(alicia, 80)

#4. Retirar 50 unidades de saldo a "Alicia".

alicia.retirar_dinero(50)


37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto . 

Código a seguir:

1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario. 
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada. 
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.

Caso de uso: 

Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


def reemplazar_palabras(texto, vieja, nueva):
    return texto.replace(vieja, nueva)

def eliminar_palabra(texto, palabra):
    return " ".join([p for p in texto.split() if p != palabra])


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción incorrecta."

#Caso de uso:

texto = "Estoy aprendiendo Python Python aprendiendo Python"

print(procesar_texto(texto, "contar"))  

#Output esperado:
#{'Estoy': 1, 'aprendiendo': 2, 'Python': 3}

print(procesar_texto(texto, "reemplazar", "Python", "SQL"))  

#Output esperado:
#Estoy aprendiendo SQL SQL aprendiendo SQL

print(procesar_texto(texto, "eliminar", "Estoy"))  

#Output esperado:
#aprendiendo Python Python aprendiendo Python



38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_dia(hora):
    if  6 <= hora < 14:
        return "Es de día"
    elif 14 <= hora < 20:
        return "Es de tarde"
    elif 20 <= hora <= 23 or 0 <= hora < 6 :
        return "Es de noche"
    else:
        return "El valor introducido no es correcto"
    

hora_proporcionada = int(input("Introduzca la hora aquí: "))

print(momento_dia(hora_proporcionada))


39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son: 

- 0 - 69 insuficiente 
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente

def determinar_calificacion(calificacion):
    if 0 <= calificacion <= 69:
        return "El alumno ha sacado un insuficiente"
    elif 70 <= calificacion <= 79:
        return "El alumno ha sacado un bien"
    elif 80 <= calificacion <= 89:
        return "El alumno ha sacado un muy bien"
    elif 90 <= calificacion <= 100:
        return "El alumno ha sacado un excelente"
    else:
        return "El valor introducido no es correcto, ya que no está entre 0 y 100"
    

calificacion_introducida = int(input("Introduzca aquí la calificación:"))

print(determinar_calificacion(calificacion_introducida))


40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura,datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura ) /2
    else:
        return "La figura intoducida no es correcta"

#Ejemplo;

print(calcular_area("rectangulo", (2, 4)))   

#Output esperado: 
#8

print(calcular_area("circulo", (5,))) 

#Output esperado: 
#78.53981633974483

print(calcular_area("triangulo", (9, 6)))

#Output esperado: 
#27.0


41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 

1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

#1. Solicita al usuario que ingrese el precio original de un artículo.

precio_original = float(input("Ingrese el precio original del articulo: "))

#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 

tiene_cupon_descuento = input("¿Tiene un cupon de descuento? (si/no) ").strip().lower()

#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 

if tiene_cupon_descuento == "si":
    descuento = float(input("Ingrese el valor del cupón de descuento: "))

#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 

    if descuento > 0:
        precio_final = precio_original - descuento
      
        print(f" Se ha aplicado un descuento de {descuento}€")
    else:
        precio_final = precio_original
        print("El descuento no es valido")

else:
    precio_final = precio_original
    print("No se ha aplicado ningun descuento")

#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.     

print(f" El precio final se queda en {precio_final}€")























