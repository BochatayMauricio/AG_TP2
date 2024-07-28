from tabulate import tabulate
class mochila:
    pass
    def __init__(self,productos):
        self.productos = productos
        peso = 0
        val = 0
        for prod in productos:
            peso+=prod.getPeso()
            val+=prod.getValor()
        self.peso = peso
        self.valor = val

    def getProductos(self):
        return self.productos
    
    def getValor(self):
        return self.valor
    
    def getPeso(self):
        return self.peso

    def mostrarMochila(self):
        datos_productos = []
        for value in self.productos:
            prod = []
            prod.append(value.getNumero())
            prod.append(value.getPeso())
            prod.append(value.getValor())
            datos_productos.append(prod)
        print(tabulate(datos_productos,headers=["Numero","Peso","Valor"]))
        print("-------------------------------------------------------")
        print("Peso total utilizado: ",self.peso)
        print("Valor total alcanzado: ",self.valor)
