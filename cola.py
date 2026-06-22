"""Implementacion de una COLA o queue usando nodos enlazados, con referencias a head (cabeza) y tail (cola). Se usa en CarUPS para gestionar los turnos de atencion. Los clientes se atienden en orden de llegada -> principio FIFO (First In, First Out): enqueue agrega al final, dequeue saca desde el inicio. Gracias a que se mantiene la referencia tail, ambas operaciones se hacen en O(1), sin recorrer la cola."""


class nodo_cola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self._tamano = 0

    def enqueue(self, dato):
        # enqueue: O(1)
        nuevo_nodo = nodo_cola(dato)
        if self.tail is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        self._tamano += 1

    def dequeue(self):
        # dequeue: O(1)
        if self.esta_vacia():
            return None
        nodo_quitado = self.head
        self.head = nodo_quitado.siguiente
        if self.head is None:
            self.tail = None
        self._tamano -= 1
        return nodo_quitado.dato

    def encolar_al_frente(self, dato):
        # O(1) - usado solo para deshacer "atender"
        nuevo_nodo = nodo_cola(dato)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo
        if self.tail is None:
            self.tail = nuevo_nodo
        self._tamano += 1

    def quitar_ultimo(self):
        # O(n) - usado solo para deshacer "registrar"
        if self.esta_vacia():
            return None
        if self.head is self.tail:
            dato = self.head.dato
            self.head = None
            self.tail = None
            self._tamano -= 1
            return dato

        actual = self.head
        while actual.siguiente is not self.tail:
            actual = actual.siguiente
        dato = self.tail.dato
        actual.siguiente = None
        self.tail = actual
        self._tamano -= 1
        return dato

    def esta_vacia(self):
        return self.head is None

    def tamano(self):
        return self._tamano

    def mostrar(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos


if __name__ == "__main__":
    print("=== Caso de prueba: Cola ===")
    c = cola()
    assert c.esta_vacia() is True
    c.enqueue(("0102030405", "Juan Perez"))
    c.enqueue(("0607080910", "Maria Lopez"))
    assert c.tamano() == 2
    assert c.dequeue() == ("0102030405", "Juan Perez")
    assert c.head.dato == ("0607080910", "Maria Lopez")
    print("Todas las pruebas de cola pasaron correctamente.")