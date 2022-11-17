# • Diseña un algoritmo que permita mostrar las tablas de multiplicar del 1 al 10
def multiplicar1():
    numMult=[1,2,3,4,5,6,7,8,9,10]
    for n1 in numMult:
        print(n1*1,n1*2,n1*3,n1*4,n1*5,n1*6,n1*7,n1*8,n1*9,n1*10)
#multiplicar1()

def multiplicar2():
    tablaD = 1 #tablas del 1...
    tablaH = 10 #...al 10
    D = 1 #multiplicaciones desde el 1...
    H = 10 #...hasta el 10

    for num1 in range(tablaD, tablaH + 1):
        print(f'Tabla de multiplicar del {num1}:') #mostramos una cabecera para cada tabla
        for num2 in range(D, H + 1):
            print(f'{num1} x {num2} = {num1 * num2}')
        print() #línea en blanco al final de cada tabla
#multiplicar2()

def multiplicar22():
    for x in range(11):
        for y in range(11):
            print(f'{x} x {y} = {x*y}')
#multiplicar22()


#AQUÍ HEMOS INTENTADO HACERLO CON PROGRAMACIÓN FUNCIONAL. HAY ERRORES QUE NO HEMOS VISTO. CARMELO TIENE QUE MIRARLO BIEN. AÚN NO TENEMOS SOLUCIÓN

# def multiplicarMap():
#     listaN=range(11)
#     print(list( map(lambda x: x*int(str(map(lambda y: y, range(11)))), listaN) ))
# multiplicarMap()


