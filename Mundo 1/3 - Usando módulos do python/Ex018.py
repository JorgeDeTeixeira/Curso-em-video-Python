from math import radians, cos, sin, tan

ang = float(input('Digite ângulo:'))
print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan(radians(ang)):.2f}')
