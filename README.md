# Desafio-Manejo de excepciones
Este repositorio consiste en los archivos para el desafio "manejo de excepciones", correspondiente al modulo 4 "python avanzado" para el bootcamp full stack python de talento digital.

## Requerimientos
- SO windows, Mac OS o Linux
- Python 3.12 o superior
- todos los archivos .py en una sola carpeta

# Proyecto de Error de dimensiones en fotos

Ingresa las dimensiones de la foto cuando se te solicite y observa cómo se manejan las excepciones si se ingresan valores fuera del rango permitido.

## Estructura del Proyecto

El proyecto incluye dos archivos principales:

1. **`error.py`**: Define la excepción personalizada `DimensionError`, que se utiliza para manejar errores cuando las dimensiones de la foto están fuera de los límites permitidos.

2. **`foto.py`**: Contiene la clase `Foto`, que representa una foto con atributos de ancho, alto y ruta. Los métodos `setter` para los atributos de ancho y alto validan los valores y lanzan la excepción `DimensionError` si los valores están fuera del rango permitido.

## Autor
Miguel Martinez F.
