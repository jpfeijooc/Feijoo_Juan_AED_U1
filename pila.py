"""Implementacion de una PILA usando nodos enlazados. Se usa en CarUPS para guardar el historial de acciones del operador. La pila funciona bajo el principio LIFO (Last In, First Out): la ultima accion que se hizo es la primera que se puede deshacer, porque para "deshacer" siempre se revierte lo mas reciente primero
(no tendria sentido deshacer una accion vieja si hay otras mas nuevas encima que dependen de ella). Por eso LIFO es el principio adecuado para un historial de deshacer"."""


class nodo_pila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class pila:
    def __init__(self):
        self.head = None
        self._tamano = 0

    def push(self, dato):
        # push: O(1)
        nuevo_nodo = nodo_pila(dato)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo
        self._tamano += 1

    def pop(self):
        # pop: O(1)
        if self.esta_vacia():
            return None
        nodo_quitado = self.head
        self.head = nodo_quitado.siguiente
        self._tamano -= 1
        return nodo_quitado.dato

    def ver_cima(self):
        if self.esta_vacia():
            return None
        return self.head.dato

    def esta_vacia(self):
        return self.head is None

    def tamano(self):
        return self._tamano

    def __len__(self):
        return self._tamano


if __name__ == "__main__":
    print("=== Caso de prueba: Pila ===")
    p = pila()
    assert p.esta_vacia() is True
    p.push(("registrar", "0102030405", "Juan Perez"))
    p.push(("atender", "0102030405", "Juan Perez"))
    assert p.tamano() == 2
    assert p.ver_cima() == ("atender", "0102030405", "Juan Perez")
    assert p.pop() == ("atender", "0102030405", "Juan Perez")
    assert p.tamano() == 1
    print("Todas las pruebas de pila pasaron correctamente.")