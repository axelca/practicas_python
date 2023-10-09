# Solicitar al usuario el total de la factura
total_factura = float(input("Por favor, ingresa el total de la factura: "))

# Calcular la propina para diferentes porcentajes
propina_18 = total_factura * 0.18
propina_20 = total_factura * 0.20
propina_25 = total_factura * 0.25

# Imprimir las propinas calculadas
print(f"Propina del 18%: ${propina_18:.2f}")
print(f"Propina del 20%: ${propina_20:.2f}")
print(f"Propina del 25%: ${propina_25:.2f}")
