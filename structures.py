class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.name} | Precio: ${self.price} | Cantidad: {self.quantity}"

class Node:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

# --- Estructura 1: Arreglo (Manejado nativamente como lista en Python, pero conceptualmente un arreglo) ---
# Se usará una lista simple en el main para esto.

# --- Estructura 2: Pila (Stack) ---
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_all(self):
        return self.items

# --- Estructura 3: Cola (Queue) ---
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def get_all(self):
        return self.items

# --- Estructura 4: Árbol Binario de Búsqueda (BST) ---
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if self.root is None:
            self.root = Node(product)
        else:
            self._insert_recursive(self.root, product)

    def _insert_recursive(self, current_node, product):
        if product.id < current_node.product.id:
            if current_node.left is None:
                current_node.left = Node(product)
            else:
                self._insert_recursive(current_node.left, product)
        elif product.id > current_node.product.id:
            if current_node.right is None:
                current_node.right = Node(product)
            else:
                self._insert_recursive(current_node.right, product)
        else:
            # ID duplicado, podríamos actualizar o ignorar. Por ahora ignoramos.
            pass

    def search(self, id):
        return self._search_recursive(self.root, id)

    def _search_recursive(self, current_node, id):
        if current_node is None:
            return None
        if id == current_node.product.id:
            return current_node.product
        elif id < current_node.product.id:
            return self._search_recursive(current_node.left, id)
        else:
            return self._search_recursive(current_node.right, id)

    def in_order_traversal(self):
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current_node, result):
        if current_node:
            self._in_order_recursive(current_node.left, result)
            result.append(current_node.product)
            self._in_order_recursive(current_node.right, result)
