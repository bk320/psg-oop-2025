class Destino:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
    
    def __str__(self):
        return f"[{self.nombre}] ➡ [{self.costo}] USD"
    
class Catalogo:
    def __init__(self):
        self.lista_destinos = []
    
    def __str__(self):
        cadena_final = "🗺    Destinos    🗺\n"
        for indice, destino in enumerate(self.lista_destinos):
            cadena_final += f"{1 + indice}. {destino}\n"
        return cadena_final
            
    def __len__(self):
        return len(self.lista_destinos)
    
    def __getitem__(self, indice):
        return self.lista_destinos[indice]
    
    def __setitem__(self, indice, valor):
        self.lista_destinos[indice] = valor
        
    def __delitem__(self, indice):
        del self.lista_destinos[indice]
        
    def __iter__(self):
        return iter(self.lista_destinos)

# Ejemplo de uso
catalogo = Catalogo()
catalogo.lista_destinos.append(Destino("Uyuni", 120))
catalogo.lista_destinos.append(Destino("Isla Incahuasi", 137))
catalogo.lista_destinos.append(Destino("Laguna Colorada", 200))
catalogo.lista_destinos.append(Destino("Toro Toro", 110))
print(catalogo)
longitud = len(catalogo)
print(f"Número de destinos: {longitud}")
destino = catalogo[0]
print(destino)

print("\nModificando un destino:")
catalogo[1] = Destino("Parque Nacional Madidi", 160)
print(catalogo)

print("\nIterando sobre el catálogo:")
for destino in catalogo:
    print(destino)
    
print("\nPrueba de eliminación:")
del catalogo[0]
print(catalogo)