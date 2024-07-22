from tabulate import tabulate
class mochila:
    pass
    def __init__(self,productos):
        self.productos = productos
        vol = 0
        val = 0
        for i in range(len(productos)):
            vol=productos[i].getVolumen()+vol
            val=productos[i].getValor()+val
        self.volumen = vol
        self.valor = val

    def getProductos(self):
        return self.productos
    
    def getValor(self):
        return self.valor
    
    def getVolumen(self):
        return self.volumen

    def mostrarMochila(self):
        datos_productos = []
        for value in self.productos:
            prod = []
            prod.append(value.getNumero())
            prod.append(value.getVolumen())
            prod.append(value.getValor())
            datos_productos.append(prod)
        print(tabulate(datos_productos,headers=["Numero","Volumen","Valor"]))
        print("-------------------------------------------------------")
        print("Volumen total utilizado: ",self.volumen)
        print("Valor total alcanzado: ",self.valor)
