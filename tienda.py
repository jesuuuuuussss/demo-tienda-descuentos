precio = 200
cantidad = 2

subtotal = precio * cantidad

if subtotal >= 300:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
