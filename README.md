# Primeros_siguientes_prediccion
En este proyecto se implemento en python un argoritmo para calcular primeros, siguientes y prediccion de una gramatica.

## Archivos del proyecto

```
- funciones.py      # Implementación de los algoritmos
- main.py           # Lector de gramáticas y ejecución
- gramaticas.txt    # Archivo de entrada con las gramáticas
```

### `funciones.py`

Contiene la clase `Grammar` que implementa los tres algoritmos:

* `Primeros()` → Calcula los conjuntos **PRIMEROS**.
* `Siguiente()` → Calcula los conjuntos **SIGUIENTES**.
* `Prediccion()` → Calcula los conjuntos de **PREDICCIÓN**.
* `Resultado()` → Muestra todos los resultados en consola.

### `main.py`

* Lee las gramáticas desde `gramaticas.txt`.
* Construye objetos `Grammar`.
* Ejecuta los algoritmos y muestra los resultados en pantalla.

### `gramaticas.txt`

Archivo de texto donde se definen las gramáticas que se quieren probar.

* Cada producción se escribe en una línea con la forma:

  ```
  NoTerminal -> terminal1 | terminal2 | ...
  ```
* El símbolo vacío se representa como **ε**.

Ejercicio 1 incluido en el proyecto:

```txt

S -> A uno B C | S dos
A -> B C D | A tres | ε
B -> D cuatro C tres | ε
C -> cinco D B | ε
D -> seis | ε
```
Ejercicio 2 (Modificar el txt para el analisis de esta gramatica)
```txt
S -> A B uno
A -> dos B | ε
B -> C D | tres | ε
C -> cuatro A B | cinco
D -> seis | ε
```

---

## Ejecución

1. Ubícate en la carpeta del proyecto:

   ```bash
   cd pri_sig_pre
   ```

2. Ejecuta el programa:

   ```bash
   python3 main.py
   ```

3. Verás en consola los resultados de cada gramática:

```
GRAMÁTICA
PRIMEROS:
  FIRST(S) = {...}
  FIRST(A) = {...}
  ...

SIGUIENTES:
  FOLLOW(S) = {...}
  FOLLOW(A) = {...}
  ...

PREDICCIÓN:
  PRED(S → A uno B C) = {...}
  ...
```
