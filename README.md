# Feijoo_Juan_AED_U1
Programa de consola en Python, sencillo que gestiona los turnos de atención del taller CarUPS.

## Estructura del proyecto

```
carups/
├── pila.py     # Pila (historial de acciones) - R1
├── cola.py     # Cola (turnos de atención)     - R2
├── lista.py    # Lista enlazada (clientes)     - R3
└── main.py     # Menú de consola que integra todo
```

## Cómo ejecutar el programa

Requisitos: Python 3.8 o superior (no requiere librerías externas).

```bash
python main.py
```

Esto abre un menú interactivo en consola:

```
===== CarUPS - Gestion de turnos =====
1. Registrar turno (nuevo cliente)
2. Atender siguiente turno
3. Deshacer ultima accion
4. Buscar cliente por nombre
5. Mostrar cola de turnos
6. Mostrar clientes registrados
7. Mostrar historial de acciones
0. Salir
```

También se puede probar cada estructura por separado (cada archivo
incluye un caso de prueba al final):

```bash
python pila.py
python cola.py
python lista.py
```

## Descripción de las estructuras

Las tres estructuras se implementan con un nodo propio (`nodo_pila`,
`nodo_cola`, `nodo_cliente`) y una clase contenedora que mantiene
referencias a los extremos de la cadena de nodos.

### R1 — Pila (`pila.py`)

Guarda el historial de acciones del operador (`registrar`, `atender`)
como nodos enlazados, con una única referencia `self.head` al último
nodo agregado (el "tope" de la pila). Se usa para implementar la
opción **"Deshacer última acción"** mediante `pop()`.

**¿Por qué LIFO es el principio adecuado?** Porque al deshacer una
acción siempre se debe revertir la **más reciente primero**: si se
intentara deshacer una acción antigua mientras hay otras más nuevas
"encima" (que pueden depender de ese estado), el sistema quedaría en
un estado inconsistente. LIFO garantiza que el "deshacer" siempre
opera sobre el último cambio realizado, igual que en un editor de
texto o cualquier sistema de Undo.

### R2 — Cola (`cola.py`)

Cola de turnos implementada con nodos enlazados y dos referencias,
`self.head` (cabeza, el próximo en ser atendido) y `self.tail`
(final, el último que llegó). Gracias a mantener ambas referencias,
tanto `enqueue` (llega un cliente) como `dequeue` (se atiende a un
cliente) se hacen en **O(1)**, sin recorrer la cola. Los clientes se
atienden en orden de llegada (FIFO), como en cualquier fila real del
taller.

### R3 — Lista enlazada (`lista.py`)

Lista simplemente enlazada que mantiene el registro histórico de
todos los clientes del taller (DNI y nombre), con una única
referencia `self.head` (cabeza). Permite agregar un cliente, buscar
por nombre (o por DNI) y mostrar la lista completa recorriéndola
nodo por nodo desde la cabeza.


## Tabla de complejidades

| Estructura | Operación              | Complejidad | Justificación                                                                 |
|------------|-------------------------|:-----------:|--------------------------------------------------------------------------------|
| Pila       | `push`                  | O(1)        | Se inserta un nuevo nodo directamente como nuevo `head`.                       |
| Pila       | `pop`                   | O(1)        | Se quita el nodo `head` y se actualiza la referencia, sin recorrer la pila.    |
| Pila       | `ver_cima`               | O(1)        | Acceso directo al nodo `head`.                                                 |
| Cola       | `enqueue`                | O(1)        | Se inserta el nuevo nodo usando la referencia `tail`, sin recorrer la cola.    |
| Cola       | `dequeue`                 | O(1)        | Se quita el nodo `head` y se actualiza la referencia, sin recorrer la cola.    |
| Cola       | `encolar_al_frente` (deshacer atender) | O(1) | Inserción directa antes de `head`.                                      |
| Cola       | `quitar_ultimo` (deshacer registrar)   | O(n) | Al ser simplemente enlazada, no hay puntero "anterior" desde `tail`; hay que recorrer hasta el penúltimo nodo. |
| Cola       | `mostrar`                 | O(n)        | Hay que recorrer todos los nodos para listarlos.                              |
| Lista      | `agregar`                  | O(n)        | Sin puntero `tail`, se recorre hasta el último nodo para mantener el orden de registro. |
| Lista      | `buscar_por_nombre` / `buscar_por_dni` | O(n) | En el peor caso hay que recorrer todos los nodos.                       |
| Lista      | `mostrar`                  | O(n)        | Se recorre toda la lista desde `head`.                                        |


## Casos de prueba incluidos

- `pila.py`: push de acciones, verificación de tamaño, cima (`ver_cima`) y pop.
- `cola.py`: enqueue de turnos, verificación de orden FIFO y dequeue.
- `lista.py`: agregar clientes, búsqueda exitosa y búsqueda fallida.
