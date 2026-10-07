def calcular_descuento(precio, tipo_cliente):
    if tipo_cliente == "VIP":
        if precio > 100:
            return precio * 0.20
        else:
            return precio * 0.10
    elif tipo_cliente == "REGULAR":
        if precio > 100:
            return precio * 0.05
        else:
            return 0
    else:
        return 0