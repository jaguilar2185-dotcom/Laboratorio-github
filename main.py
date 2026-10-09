from ventas import calcular_total
 
print("=== SISTEMA DE VENTAS ===")
 
producto = "Laptop"
precio = 40000
cantidad = 2
 
total = calcular_total(precio, cantidad)
 
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Total: ₡{total:,.2f}")