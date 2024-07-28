import inventario
import producto
import mochila_ex
import time
#Tiempo de inicio de ejecucion
inicio = time.time()

#La matriz de subconjuntos
conjuntos = []
#peso maximo mochila en gr
pesoMax = 3000
#creo la instancia del inventario
inv = inventario.inventario()
def inicializacion():
    prod1 = producto.producto(1,72,1800)
    inv.agregarProducto(prod1)
    prod2 = producto.producto(2,36,600)
    inv.agregarProducto(prod2)
    prod3 = producto.producto(3,60,1200)
    inv.agregarProducto(prod3)

    #muestro inventario
    for i in range(len(inv.getInventario())):
        print(  inv.getInventario()[i].getPeso(),'--',
                 inv.getInventario()[i].getValor() )
    cantidad = len(inv.getInventario())
    return cantidad,inv.getInventario()

#generamos todos los subconjuntos posibles, sin importar si cumple o no con la capacidad
def generarSubconjuntos(cantidad_productos):
    #hacemos arreglo de 10 posiciones en binario, donde hay 1 es la posicion del elemento del inventario que pertece al subconjunto
    #y las filas son para cada subconjuntos, es decir, una fila es un subconjunto de 10 posiciones
    #basicamente es una matriz de 1024 x cantidad_prod
    conjuntos = [] #matriz
    for i in range(2**cantidad_productos):
        subconjunto = [] #vector fila de la matriz
        for j in range(cantidad_productos):
            if((i & (2**j)) > 0): #esto nos permite corrernos un digito a la izq. en el binario
                subconjunto.insert(j,1)
            else:
                subconjunto.insert(j,0)
        conjuntos.append(subconjunto)
    return conjuntos

def elegirMejor(productos:list,conjuntos:list):
    indiceOptimo=-1
    maxValor = 0
    for subcon in conjuntos:
        pesoSubConjunto = 0
        sum = 0
        for i in range(len(subcon)):
            if(subcon[i]==1):
                sum = sum + productos[i].getValor()
                pesoSubConjunto = pesoSubConjunto + productos[i].getPeso()
        if(sum>maxValor and pesoSubConjunto <= pesoMax):
            maxValor = sum
            indiceOptimo = conjuntos.index(subcon)
    print(indiceOptimo)
    return conjuntos[indiceOptimo]

#Esta funcion devuelve un arreglo de objetos producto para cargar la mochila
def productosSeleccionados(mejorSubconjunto):
    return inv.buscarProductos(mejorSubconjunto)


#principal
cantidad_productos,inventario=inicializacion()
conjuntos=generarSubconjuntos(cantidad_productos)
mejorSubconjunto = elegirMejor(inventario,conjuntos)
#creamos la instancia de la mochila
productosSelec:list = productosSeleccionados(mejorSubconjunto)
mochila = mochila_ex.mochila(productosSelec)
#Mostramos la mochila
mochila.mostrarMochila()
fin = time.time()
print("Tiempo de ejecucion",(fin-inicio)*(10**3),"ms")

