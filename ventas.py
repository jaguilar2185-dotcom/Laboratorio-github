def calcular_total(precio, cantidad):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
 
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")
 
    return precio * cantidad