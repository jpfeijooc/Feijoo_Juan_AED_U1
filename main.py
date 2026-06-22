from pila import pila
from cola import cola
from lista import lista_clientes

historial_acciones = pila()
turnos = cola()
clientes = lista_clientes()

def mostrar_menu():
    print("\n===== CarUPS - Gestion de turnos =====")
    print("1. Registrar turno (nuevo cliente)")
    print("2. Atender siguiente turno")
    print("3. Deshacer ultima accion")
    print("4. Buscar cliente por nombre")
    print("5. Mostrar cola de turnos")
    print("6. Mostrar clientes registrados")
    print("7. Mostrar historial de acciones")
    print("0. Salir")

def pedir_dni_nombre():
    dni = input("DNI del cliente: ").strip()
    nombre = input("Nombre del cliente: ").strip()
    return dni, nombre

def registrar_turno():
    dni, nombre = pedir_dni_nombre()
    if not dni or not nombre:
        print("DNI y nombre son obligatorios. Operacion cancelada.")
        return

    if clientes.buscar_por_dni(dni) is None:
        clientes.agregar(dni, nombre)

    turnos.enqueue((dni, nombre))

    historial_acciones.push(("registrar", dni, nombre))

    print(f"Turno registrado para {nombre} (DNI: {dni}).")

def atender_turno():
    if turnos.esta_vacia():
        print("No hay turnos en espera.")
        return

    dni, nombre = turnos.dequeue()
    historial_acciones.push(("atender", dni, nombre))
    print(f"Atendiendo a {nombre} (DNI: {dni}).")

def deshacer_accion():
    if historial_acciones.esta_vacia():
        print("No hay acciones para deshacer.")
        return

    accion = historial_acciones.pop()
    tipo, dni, nombre = accion

    if tipo == "registrar":
        turnos.quitar_ultimo()
        print(f"Se deshizo el registro del turno de {nombre} (DNI: {dni}).")
    elif tipo == "atender":
        turnos.encolar_al_frente((dni, nombre))
        print(f"Se deshizo la atencion de {nombre} (DNI: {dni}); vuelve a la cola.")

def buscar_cliente():
    nombre = input("Nombre a buscar: ").strip()
    encontrado = clientes.buscar_por_nombre(nombre)
    if encontrado is None:
        print("Cliente no encontrado.")
    else:
        print(f"Cliente encontrado -> DNI: {encontrado.dni}, Nombre: {encontrado.nombre}")

def mostrar_cola_turnos():
    elementos = turnos.mostrar()
    if not elementos:
        print("No hay turnos en espera.")
        return
    print("Cola de turnos (orden de atencion):")
    for i, (dni, nombre) in enumerate(elementos, start=1):
        print(f"   {i}. {nombre} (DNI: {dni})")

def mostrar_clientes_registrados():
    elementos = clientes.mostrar()
    if not elementos:
        print("No hay clientes registrados.")
        return
    print("Clientes registrados:")
    for dni, nombre in elementos:
        print(f"   - {nombre} (DNI: {dni})")

def mostrar_historial():
    if historial_acciones.esta_vacia():
        print("No hay acciones registradas.")
        return
    print("Historial de acciones (de la mas reciente a la mas antigua):")
    nodo = historial_acciones.head
    contador = 1
    while nodo is not None:
        tipo, dni, nombre = nodo.dato
        print(f"   {contador}. {tipo} -> {nombre} (DNI: {dni})")
        nodo = nodo.siguiente
        contador += 1

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_turno()
        elif opcion == "2":
            atender_turno()
        elif opcion == "3":
            deshacer_accion()
        elif opcion == "4":
            buscar_cliente()
        elif opcion == "5":
            mostrar_cola_turnos()
        elif opcion == "6":
            mostrar_clientes_registrados()
        elif opcion == "7":
            mostrar_historial()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

if __name__ == "__main__":
    main()