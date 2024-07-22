from tabulate import tabulate
class mochila_heuristico:
    productos=[]
    capacidad=4200
    valor=0

    def setProducto(self,producto):
        if(producto.getVolumen()<=self.capacidad):
            self.productos.append(producto)
            self.capacidad = self.capacidad - producto.getVolumen()
            self.valor = self.valor + producto.getValor()

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
        print("Volumen total utilizado: ",4200-self.capacidad)
        print("Valor total alcanzado: ",self.valor)