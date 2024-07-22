class inventario:
    inventario: list = []
    
    def agregarProducto(self,prodn):
        self.inventario.append(prodn)

    def getInventario(self):
        return self.inventario

    def mostrar(self):
        print(self.inventario)

    def buscarProductos(self,subconjuntoSel:list):
        productos = []
        for j in range(len(subconjuntoSel)):
            if(subconjuntoSel[j]==1):
                productos.append(self.inventario[j])
        return productos