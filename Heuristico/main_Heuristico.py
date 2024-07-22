import inventario
import producto
from mochila_heuristico import mochila_heuristico

#creo la instancia del inventario
inv = inventario.inventario()
def inicializacion():
    prod1 = producto.producto(1,20,150)
    inv.agregarProducto(prod1)
    prod2 = producto.producto(2,40,325)
    inv.agregarProducto(prod2)
    prod3 = producto.producto(3,50,600)
    inv.agregarProducto(prod3)
    prod4 = producto.producto(4,36,805)
    inv.agregarProducto(prod4)
    prod5 = producto.producto(5,25,430)
    inv.agregarProducto(prod5)
    prod6 = producto.producto(6,64,1200)
    inv.agregarProducto(prod6)
    prod7 = producto.producto(7,54,770)
    inv.agregarProducto(prod7)
    prod8 = producto.producto(8,18,60)
    inv.agregarProducto(prod8)
    prod9 = producto.producto(9,46,930)
    inv.agregarProducto(prod9)
    prod10 = producto.producto(10,28,353)
    inv.agregarProducto(prod10)

    #muestro inventario
    for i in range(len(inv.getInventario())):
        print(  inv.getInventario()[i].getVolumen(),'--',
                 inv.getInventario()[i].getValor() )
    return inv.getInventario()

def calcularProporcion(inventario:list):
    proporciones=[] #necesitamos que sea bidimensional ya que hay que ordenarlo
    for prod in inventario:
        propor_prod = [] #en la primera posicion el numero y en la segunda la proporcion calculada
        propor_prod.insert(0,prod.getNumero())
        propor_prod.insert(1,(prod.getValor()/prod.getVolumen()))
        proporciones.append(propor_prod)
    proporciones_ordenada=sorted(proporciones,key=lambda x:x[1]) #con esta linea ordenamos de menor a mayor
    return proporciones_ordenada

def cargarMochila(porporciones_ord:list,inventario:list,mochila:mochila_heuristico):
    porporciones_invertida=list(reversed(porporciones_ord)) #utilizamos reverse porque es mejor si está ordenada de mayor a menor
    print(porporciones_invertida)
    for p in porporciones_invertida: 
        prod_seleccionado = inventario[p[0]-1]
        mochila.setProducto(prod_seleccionado)

inventario=inicializacion()
proporciones=calcularProporcion(inventario)
print(proporciones)
#creamos la instancia de la mochila
mochila = mochila_heuristico()
cargarMochila(proporciones,inventario,mochila)
mochila.mostrarMochila()