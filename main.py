import sys
from structures import Product, Stack, Queue, BinaryTree

# --- Inicialización de Estructuras ---
inventory_list = [] # Arreglo
pallet_stack = Stack() # Pila
order_queue = Queue() # Cola
product_tree = BinaryTree() # Árbol Binario

def print_menu():
    print("\n--- SISTEMA DE GESTIÓN DE BODEGA ---")
    print("1. Gestionar Inventario (Arreglo/Lista)")
    print("2. Gestionar Pallets (Pila)")
    print("3. Gestionar Pedidos (Cola)")
    print("4. Buscar Producto (Árbol Binario)")
    print("5. Salir")

def manage_inventory():
    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Ver todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            if not inventory_list:
                print("El inventario está vacío.")
            else:
                print("\nListado de Productos:")
                for p in inventory_list:
                    print(p)
        elif choice == '2':
            try:
                id = int(input("Ingrese ID del producto: "))
                # Verificar si ya existe en el árbol para evitar duplicados de ID
                if product_tree.search(id):
                    print("Error: Ya existe un producto con ese ID.")
                    continue
                
                name = input("Ingrese nombre del producto: ")
                price = float(input("Ingrese precio del producto: "))
                quantity = int(input("Ingrese cantidad inicial: "))
                
                new_product = Product(id, name, price, quantity)
                
                # Agregar a Arreglo
                inventory_list.append(new_product)
                # Agregar a Árbol
                product_tree.insert(new_product)
                
                print("Producto agregado exitosamente.")
            except ValueError:
                print("Error: Entrada inválida. Por favor ingrese números donde corresponda.")
        elif choice == '3':
            break
        else:
            print("Opción no válida.")

def manage_pallets():
    while True:
        print("\n--- GESTIÓN DE PALLETS (PILA) ---")
        print("1. Ver estado del pallet actual (Tope de la pila)")
        print("2. Apilar producto (Push)")
        print("3. Desapilar producto (Pop)")
        print("4. Ver todos los items en el pallet")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            top = pallet_stack.peek()
            if top:
                print(f"Tope del pallet: {top}")
            else:
                print("El pallet está vacío.")
        elif choice == '2':
            # Para simplificar, apilamos productos existentes del inventario
            try:
                id = int(input("Ingrese ID del producto a apilar: "))
                product = product_tree.search(id)
                if product:
                    pallet_stack.push(product)
                    print(f"Producto '{product.name}' apilado.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Error: ID inválido.")
        elif choice == '3':
            popped = pallet_stack.pop()
            if popped:
                print(f"Producto desapilado: {popped}")
            else:
                print("No hay productos para desapilar.")
        elif choice == '4':
            items = pallet_stack.get_all()
            if items:
                print("\nContenido del Pallet (Base -> Tope):")
                for p in items:
                    print(p)
            else:
                print("El pallet está vacío.")
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

def manage_orders():
    while True:
        print("\n--- GESTIÓN DE PEDIDOS (COLA) ---")
        print("1. Ver próximo pedido a procesar")
        print("2. Agregar pedido (Enqueue)")
        print("3. Procesar pedido (Dequeue)")
        print("4. Ver todos los pedidos pendientes")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            next_order = order_queue.peek()
            if next_order:
                print(f"Próximo pedido: {next_order}")
            else:
                print("No hay pedidos pendientes.")
        elif choice == '2':
             # Simulamos un pedido como un producto solicitado
            try:
                id = int(input("Ingrese ID del producto solicitado: "))
                product = product_tree.search(id)
                if product:
                    order_queue.enqueue(product)
                    print(f"Pedido para '{product.name}' agregado a la cola.")
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Error: ID inválido.")
        elif choice == '3':
            processed = order_queue.dequeue()
            if processed:
                print(f"Pedido procesado: {processed}")
            else:
                print("No hay pedidos para procesar.")
        elif choice == '4':
            items = order_queue.get_all()
            if items:
                print("\nPedidos Pendientes (Próximo -> Último):")
                # La lista interna de Queue tiene el último en index 0 por el insert(0), 
                # pero conceptualmente queremos ver el orden de llegada.
                # Ajustamos visualización: el que sale primero es items[-1] en nuestra impl de Queue
                # Vamos a mostrarlo tal cual está almacenado para depuración o invertirlo.
                # Nuestra Queue: insert(0) -> enqueue. pop() -> dequeue (saca del final).
                # Entonces items[-1] es el frente (front).
                for p in reversed(items):
                     print(p)
            else:
                print("No hay pedidos pendientes.")
        elif choice == '5':
            break
        else:
            print("Opción no válida.")

def search_product():
    print("\n--- BÚSQUEDA DE PRODUCTO (ÁRBOL BINARIO) ---")
    try:
        id = int(input("Ingrese ID del producto a buscar: "))
        product = product_tree.search(id)
        if product:
            print("\nProducto Encontrado:")
            print(product)
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("Error: ID inválido.")
    input("Presione Enter para continuar...")

def main():
    while True:
        print_menu()
        choice = input("Seleccione una opción: ")

        if choice == '1':
            manage_inventory()
        elif choice == '2':
            manage_pallets()
        elif choice == '3':
            manage_orders()
        elif choice == '4':
            search_product()
        elif choice == '5':
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
