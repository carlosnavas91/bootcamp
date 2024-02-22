
Punto de partida:
- Conocemos el mensaje encriptado.
- Conocemos la correspondencia, la cual es el alfabeto numero con la posición de cada letra en el mismo.
- Sabemos que el mensaje esta en ingles
- Sabemos que existe un desfase entre la correspondencia de cada caracter del mensaje encriptado vs la posición de cada caracter en el alfabeto

Desarrollo:
- Crear un diccionario con la correspondencia entre caracter y posición (valor)
- Iterar el mensaje encriptado hasta un maximo de 27 veces:
  - sacar el primer caracter del mensaje,
  - aplicarle el desfase de la iteración, 
  - construir un nuevo mensaje (desencriptado), obteniendo el caracter correspodiente a la nueva posición en el alfabeto (es decir, más el desfase)
- Finalmente validar si el nuevo mensaje hace sentido (esta escrito en ingles):
  - buscar palabras comunes del idioma dentro del nuevo mensaje, si coincide: romper el ciclo y terminar la ejecución; sino, continuar con el ciclo, sumando una posición al desfase

  