from tabulate import tabulate
class mochila_heuristico:
    productos=[]
    pesoMaximo=3000
    valor=0

    def setProducto(self,producto):
        if(producto.getPeso()<=self.pesoMaximo):
            self.productos.append(producto)
            self.pesoMaximo = self.pesoMaximo - producto.getPeso()
            self.valor = self.valor + producto.getValor()

    def mostrarMochila(self):
        datos_productos = []
        for value in self.productos:
            prod = []
            prod.append(value.getNumero())
            prod.append(value.getPeso())
            prod.append(value.getValor())
            datos_productos.append(prod)
        print(tabulate(datos_productos,headers=["Numero","Volumen","Valor"]))
        print("-------------------------------------------------------")
        print("Volumen total utilizado: ",3000-self.pesoMaximo)
        print("Valor total alcanzado: ",self.valor)