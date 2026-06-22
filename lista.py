
"""Implementacion de una LISTA simple enlazada usando nodos. Se usa en CarUPS para mantener el registro de todos los clientes que han pasado por el taller: agregar cliente, buscar por nombre o DNI y mostrar la lista completa recorriendola desde la cabeza."""


class nodo_cliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.siguiente = None


class lista_clientes:
    def __init__(self):
        self.head = None
        self._tamano = 0

    def agregar(self, dni, nombre):
        nuevo_nodo = nodo_cliente(dni, nombre)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self._tamano += 1

    def buscar_por_nombre(self, nombre):
        actual = self.head
        while actual is not None:
            if actual.nombre.strip().lower() == nombre.strip().lower():
                return actual
            actual = actual.siguiente
        return None

    def buscar_por_dni(self, dni):
        actual = self.head
        while actual is not None:
            if actual.dni == dni:
                return actual
            actual = actual.siguiente
        return None

    def mostrar(self):
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append((actual.dni, actual.nombre))
            actual = actual.siguiente
        return elementos

    def tamano(self):
        return self._tamano


if __name__ == "__main__":
    print("=== Caso de prueba: lista_clientes ===")
    l = lista_clientes()
    l.agregar("0102030405", "Juan Perez")
    l.agregar("0607080910", "Maria Lopez")
    assert l.tamano() == 2
    encontrado = l.buscar_por_nombre("maria lopez")
    assert encontrado is not None and encontrado.dni == "0607080910"
    assert l.buscar_por_nombre("Carlos Ramirez") is None
    print("Todas las pruebas de lista_clientes pasaron correctamente.")