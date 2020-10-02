# 1. PRÁCTICA OPERACIONES.

# Calcular la aproximación al seno de un ángulo X expresado en grados.

# sin(90) = 1.0
# sin(45) = 0.707
# sin(50) = 0.766

x = 90
parenthesis_1 = 180 - x
numerator = 4 * x * parenthesis_1
denominator = 40500 - x * parenthesis_1

sin = numerator / denominator

print(sin)