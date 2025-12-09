"""
================================================================================
SISTEMA DE GESTIÓN - CLÍNICA VETERINARIA "PET MARKET"
================================================================================
Proyecto Final de Estructuras de Datos
Autor: Estudiante Universitario
Fecha: Diciembre 2025

Descripción:
    Este sistema gestiona una clínica veterinaria real utilizando 4 estructuras
    de datos implementadas manualmente desde cero:
    1. PILA (Stack) - Para el historial médico de cada mascota (LIFO)
    2. COLA (Queue) - Para la sala de espera (FIFO)
    3. ÁRBOL BINARIO DE BÚSQUEDA (BST) - Base de datos de mascotas
    4. ARREGLO (List) - Catálogo de servicios fijos

Nota: Todo el código está implementado en Python puro, sin librerías externas.
================================================================================
"""


# ==============================================================================
# CLASE NODO - Base para todas las estructuras enlazadas
# ==============================================================================
class Nodo:
    """
    Clase Nodo genérica que sirve como bloque de construcción para
    las estructuras de datos enlazadas (Pila, Cola, Árbol).
    
    Atributos:
        dato: El contenido que almacena el nodo (puede ser cualquier tipo)
        siguiente: Puntero/referencia al siguiente nodo (usado en Pila y Cola)
        izquierdo: Puntero al hijo izquierdo (usado en Árbol Binario)
        derecho: Puntero al hijo derecho (usado en Árbol Binario)
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo.
        
        Args:
            dato: El valor o información que guardará este nodo
        """
        self.dato = dato          # El contenido del nodo
        self.siguiente = None     # Puntero al siguiente nodo (para Pila/Cola)
        self.izquierdo = None     # Puntero hijo izquierdo (para Árbol)
        self.derecho = None       # Puntero hijo derecho (para Árbol)


# ==============================================================================
# CLASE PILA (STACK) - Estructura LIFO (Last In, First Out)
# ==============================================================================
class Pila:
    """
    Implementación manual de una Pila (Stack) usando nodos enlazados.
    
    Característica Principal: LIFO (Last In, First Out)
    - El último elemento que entra es el primero que sale.
    - Perfecta para el historial médico: el diagnóstico más reciente
      aparece primero al consultar.
    
    Uso en el Sistema:
        Cada mascota tiene una pila para su historial médico.
        Cuando se agrega un nuevo diagnóstico, se "apila" encima de los anteriores.
    """
    
    def __init__(self):
        """
        Constructor de la Pila.
        Inicializa una pila vacía donde 'tope' apunta a None.
        """
        self.tope = None      # Referencia al elemento superior de la pila
        self.tamanio = 0      # Contador de elementos en la pila
    
    def esta_vacia(self):
        """
        Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila no tiene elementos, False en caso contrario
        """
        return self.tope is None
    
    def apilar(self, dato):
        """
        Inserta un nuevo elemento en el tope de la pila (operación PUSH).
        
        Lógica:
            1. Crear un nuevo nodo con el dato
            2. El nuevo nodo apunta al tope actual
            3. El nuevo nodo se convierte en el nuevo tope
        
        Args:
            dato: El elemento a insertar en la pila
        
        Complejidad: O(1) - Tiempo constante
        """
        nuevo_nodo = Nodo(dato)           # Paso 1: Crear nuevo nodo
        nuevo_nodo.siguiente = self.tope  # Paso 2: Enlazar al tope actual
        self.tope = nuevo_nodo            # Paso 3: Actualizar el tope
        self.tamanio += 1                 # Incrementar contador
    
    def desapilar(self):
        """
        Elimina y retorna el elemento del tope de la pila (operación POP).
        
        Lógica:
            1. Verificar que la pila no esté vacía
            2. Guardar el dato del tope
            3. Mover el tope al siguiente elemento
            4. Retornar el dato guardado
        
        Returns:
            El dato del elemento eliminado, o None si la pila está vacía
        
        Complejidad: O(1) - Tiempo constante
        """
        if self.esta_vacia():
            return None
        
        dato_eliminado = self.tope.dato   # Guardar el dato antes de eliminar
        self.tope = self.tope.siguiente   # Mover tope al siguiente
        self.tamanio -= 1                 # Decrementar contador
        return dato_eliminado
    
    def ver_tope(self):
        """
        Consulta el elemento del tope sin eliminarlo (operación PEEK).
        
        Returns:
            El dato del tope, o None si la pila está vacía
        """
        if self.esta_vacia():
            return None
        return self.tope.dato
    
    def mostrar_historial(self):
        """
        Muestra todos los elementos de la pila sin modificarla.
        Recorre desde el tope hasta el final.
        
        Uso: Mostrar el historial médico completo de una mascota.
        """
        if self.esta_vacia():
            print("    📋 No hay registros en el historial.")
            return
        
        actual = self.tope
        numero_registro = 1
        
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║              📋 HISTORIAL MÉDICO COMPLETO                  ║")
        print("    ╠════════════════════════════════════════════════════════════╣")
        
        while actual is not None:
            # Si es el primer registro, marcarlo como más reciente
            if numero_registro == 1:
                print(f"    ║ 🔴 [{numero_registro}] {actual.dato}")
                print("    ║     ↑ (Más reciente)")
            else:
                print(f"    ║ ⚪ [{numero_registro}] {actual.dato}")
            
            actual = actual.siguiente
            numero_registro += 1
        
        print("    ╚════════════════════════════════════════════════════════════╝")
        print(f"    Total de registros: {self.tamanio}")


# ==============================================================================
# CLASE COLA (QUEUE) - Estructura FIFO (First In, First Out)
# ==============================================================================
class Cola:
    """
    Implementación manual de una Cola (Queue) usando nodos enlazados.
    
    Característica Principal: FIFO (First In, First Out)
    - El primer elemento que entra es el primero que sale.
    - Perfecta para la sala de espera: el primer paciente en llegar
      es el primero en ser atendido.
    
    Uso en el Sistema:
        Gestiona la sala de espera de la veterinaria.
        Las mascotas se encolan al llegar y se desencolan al ser atendidas.
    
    Nota Importante:
        NO usamos list.pop(0) que sería O(n). Implementamos con punteros
        para lograr O(1) en ambas operaciones.
    """
    
    def __init__(self):
        """
        Constructor de la Cola.
        Mantiene dos punteros: frente (para desencolar) y final (para encolar).
        """
        self.frente = None    # Puntero al primer elemento (sale primero)
        self.final = None     # Puntero al último elemento (entra último)
        self.tamanio = 0      # Contador de elementos en la cola
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        
        Returns:
            bool: True si la cola no tiene elementos, False en caso contrario
        """
        return self.frente is None
    
    def encolar(self, dato):
        """
        Inserta un nuevo elemento al final de la cola (operación ENQUEUE).
        
        Lógica:
            1. Crear un nuevo nodo con el dato
            2. Si la cola está vacía, frente y final apuntan al nuevo nodo
            3. Si no, el final actual apunta al nuevo nodo, y actualizamos final
        
        Args:
            dato: El elemento a insertar en la cola
        
        Complejidad: O(1) - Tiempo constante gracias al puntero 'final'
        """
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            # Caso especial: cola vacía
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            # Caso normal: agregar al final
            self.final.siguiente = nuevo_nodo  # El último apunta al nuevo
            self.final = nuevo_nodo            # Actualizar puntero final
        
        self.tamanio += 1
    
    def desencolar(self):
        """
        Elimina y retorna el elemento del frente de la cola (operación DEQUEUE).
        
        Lógica:
            1. Verificar que la cola no esté vacía
            2. Guardar el dato del frente
            3. Mover el frente al siguiente elemento
            4. Si la cola queda vacía, actualizar también el puntero final
            5. Retornar el dato guardado
        
        Returns:
            El dato del elemento eliminado, o None si la cola está vacía
        
        Complejidad: O(1) - Tiempo constante
        """
        if self.esta_vacia():
            return None
        
        dato_eliminado = self.frente.dato     # Guardar dato
        self.frente = self.frente.siguiente   # Mover frente al siguiente
        
        # Si la cola quedó vacía, actualizar también el puntero final
        if self.frente is None:
            self.final = None
        
        self.tamanio -= 1
        return dato_eliminado
    
    def ver_frente(self):
        """
        Consulta el elemento del frente sin eliminarlo (operación FRONT/PEEK).
        
        Returns:
            El dato del frente, o None si la cola está vacía
        """
        if self.esta_vacia():
            return None
        return self.frente.dato
    
    def mostrar_sala_espera(self):
        """
        Muestra todos los elementos de la cola sin modificarla.
        Visualiza la sala de espera con el orden de atención.
        """
        if self.esta_vacia():
            print("    🏥 La sala de espera está vacía. No hay pacientes esperando.")
            return
        
        actual = self.frente
        posicion = 1
        
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║                   🏥 SALA DE ESPERA                        ║")
        print("    ╠════════════════════════════════════════════════════════════╣")
        
        while actual is not None:
            mascota = actual.dato
            if posicion == 1:
                print(f"    ║ 🔴 Posición {posicion}: {mascota.nombre} (ID: {mascota.id})")
                print("    ║     ↑ (Siguiente en ser atendido)")
            else:
                print(f"    ║ ⚪ Posición {posicion}: {mascota.nombre} (ID: {mascota.id})")
            
            actual = actual.siguiente
            posicion += 1
        
        print("    ╚════════════════════════════════════════════════════════════╝")
        print(f"    Total de pacientes en espera: {self.tamanio}")


# ==============================================================================
# CLASE ÁRBOL BINARIO DE BÚSQUEDA (BST) - Base de Datos Principal
# ==============================================================================
class ArbolBinario:
    """
    Implementación manual de un Árbol Binario de Búsqueda (Binary Search Tree).
    
    Característica Principal:
    - Para cada nodo: todos los valores menores están a la izquierda,
      y todos los valores mayores están a la derecha.
    - Permite búsquedas eficientes O(log n) en el caso promedio.
    
    Uso en el Sistema:
        Funciona como la base de datos principal de mascotas.
        - Insertar mascotas ordenadas por su ID único
        - Buscar mascotas rápidamente por su ID
    
    Ventaja sobre una lista:
        En una lista, buscar un elemento es O(n).
        En un BST balanceado, buscar es O(log n).
    """
    
    def __init__(self):
        """
        Constructor del Árbol Binario de Búsqueda.
        Inicializa un árbol vacío donde la raíz apunta a None.
        """
        self.raiz = None    # Referencia al nodo raíz del árbol
        self.cantidad = 0   # Contador de nodos en el árbol
    
    def esta_vacio(self):
        """
        Verifica si el árbol está vacío.
        
        Returns:
            bool: True si el árbol no tiene nodos, False en caso contrario
        """
        return self.raiz is None
    
    def insertar(self, mascota):
        """
        Inserta una nueva mascota en el árbol ordenada por su ID.
        
        Lógica:
            1. Si el árbol está vacío, la mascota se convierte en la raíz
            2. Si no, buscar la posición correcta comparando IDs
            3. Si el ID es menor, ir a la izquierda; si es mayor, ir a la derecha
            4. Insertar cuando encontremos un espacio vacío
        
        Args:
            mascota: Objeto Mascota a insertar
        
        Returns:
            bool: True si se insertó correctamente, False si el ID ya existe
        """
        nuevo_nodo = Nodo(mascota)
        
        if self.esta_vacio():
            # Caso especial: árbol vacío
            self.raiz = nuevo_nodo
            self.cantidad += 1
            return True
        
        # Buscar la posición correcta para insertar
        actual = self.raiz
        
        while True:
            # Comparar el ID de la mascota nueva con el nodo actual
            if mascota.id < actual.dato.id:
                # Ir hacia la izquierda
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    self.cantidad += 1
                    return True
                else:
                    actual = actual.izquierdo
            elif mascota.id > actual.dato.id:
                # Ir hacia la derecha
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    self.cantidad += 1
                    return True
                else:
                    actual = actual.derecho
            else:
                # El ID ya existe, no se permite duplicados
                return False
    
    def buscar(self, id_mascota):
        """
        Busca una mascota en el árbol por su ID.
        
        Lógica:
            1. Comenzar desde la raíz
            2. Si el ID buscado es menor, ir a la izquierda
            3. Si el ID buscado es mayor, ir a la derecha
            4. Si es igual, encontramos la mascota
            5. Si llegamos a None, la mascota no existe
        
        Args:
            id_mascota: El ID único de la mascota a buscar
        
        Returns:
            Objeto Mascota si se encuentra, None si no existe
        
        Complejidad: O(log n) en promedio, O(n) en el peor caso (árbol degenerado)
        """
        actual = self.raiz
        
        while actual is not None:
            if id_mascota < actual.dato.id:
                actual = actual.izquierdo      # Buscar en subárbol izquierdo
            elif id_mascota > actual.dato.id:
                actual = actual.derecho        # Buscar en subárbol derecho
            else:
                return actual.dato             # ¡Encontrado!
        
        return None  # No se encontró la mascota
    
    def recorrido_inorden(self, nodo=None, primera_llamada=True):
        """
        Recorre el árbol en orden (In-Order Traversal).
        
        Orden de visita: Izquierdo -> Raíz -> Derecho
        Resultado: Los elementos se muestran ordenados por ID de menor a mayor.
        
        Este método es recursivo y muestra todas las mascotas ordenadas.
        
        Args:
            nodo: Nodo actual en la recursión (None inicia desde la raíz)
            primera_llamada: Flag para saber si es la primera llamada
        """
        if primera_llamada:
            nodo = self.raiz
            if self.esta_vacio():
                print("    📭 La base de datos está vacía.")
                return
            print("    ╔════════════════════════════════════════════════════════════╗")
            print("    ║             🗃️  BASE DE DATOS DE MASCOTAS                  ║")
            print("    ╠════════════════════════════════════════════════════════════╣")
        
        if nodo is not None:
            # Recorrer subárbol izquierdo
            self.recorrido_inorden(nodo.izquierdo, False)
            
            # Visitar nodo actual (mostrar mascota)
            mascota = nodo.dato
            print(f"    ║ 🐾 ID: {mascota.id} | {mascota.nombre} | Dueño: {mascota.nombre_dueno}")
            
            # Recorrer subárbol derecho
            self.recorrido_inorden(nodo.derecho, False)
        
        if primera_llamada:
            print("    ╚════════════════════════════════════════════════════════════╝")
            print(f"    Total de mascotas registradas: {self.cantidad}")


# ==============================================================================
# CLASE MASCOTA - Entidad principal del sistema
# ==============================================================================
class Mascota:
    """
    Representa a una mascota registrada en la clínica veterinaria.
    
    Cada mascota tiene:
    - Datos identificativos (id, nombre, raza)
    - Información médica (alergias)
    - Datos del dueño (nombre, celular)
    - Su propio historial médico (implementado como una Pila)
    
    Atributos:
        id (int): Identificador único de la mascota (clave para el BST)
        nombre (str): Nombre de la mascota
        raza (str): Raza o especie de la mascota
        alergias (str): Alergias conocidas de la mascota
        nombre_dueno (str): Nombre del propietario
        celular (str): Número de contacto del propietario
        historial_medico (Pila): Pila con el historial de diagnósticos
    """
    
    def __init__(self, id, nombre, raza, alergias, nombre_dueno, celular):
        """
        Constructor de la clase Mascota.
        
        Args:
            id: Identificador único (número entero)
            nombre: Nombre de la mascota
            raza: Raza o especie
            alergias: Información sobre alergias
            nombre_dueno: Nombre del propietario
            celular: Teléfono de contacto
        """
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.alergias = alergias
        self.nombre_dueno = nombre_dueno
        self.celular = celular
        
        # IMPORTANTE: Cada mascota tiene su propio historial médico
        # implementado como una Pila (LIFO)
        self.historial_medico = Pila()
    
    def mostrar_informacion(self):
        """
        Muestra toda la información de la mascota de forma formateada.
        """
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║                  🐾 FICHA DE LA MASCOTA                    ║")
        print("    ╠════════════════════════════════════════════════════════════╣")
        print(f"    ║  🆔 ID:               {self.id}")
        print(f"    ║  📛 Nombre:           {self.nombre}")
        print(f"    ║  🐕 Raza:             {self.raza}")
        print(f"    ║  ⚠️  Alergias:         {self.alergias}")
        print(f"    ║  👤 Dueño:            {self.nombre_dueno}")
        print(f"    ║  📱 Celular:          {self.celular}")
        print(f"    ║  📋 Registros:        {self.historial_medico.tamanio} diagnósticos")
        print("    ╚════════════════════════════════════════════════════════════╝")
    
    def agregar_diagnostico(self, diagnostico):
        """
        Agrega un nuevo diagnóstico al historial médico de la mascota.
        
        Args:
            diagnostico: String con la descripción del diagnóstico
        """
        self.historial_medico.apilar(diagnostico)
    
    def ver_historial(self):
        """
        Muestra el historial médico completo de la mascota.
        """
        print(f"\n    📋 Historial Médico de {self.nombre} (ID: {self.id}):")
        self.historial_medico.mostrar_historial()


# ==============================================================================
# CATÁLOGO DE SERVICIOS - Implementado como Arreglo (List)
# ==============================================================================
CATALOGO_SERVICIOS = [
    {"nombre": "Consulta General", "precio": 30.00, "codigo": "CON"},
    {"nombre": "Vacunación", "precio": 50.00, "codigo": "VAC"},
    {"nombre": "Baño y Corte", "precio": 25.00, "codigo": "BAN"},
    {"nombre": "Desparasitación", "precio": 35.00, "codigo": "DES"},
    {"nombre": "Cirugía Menor", "precio": 150.00, "codigo": "CIR"},
    {"nombre": "Rayos X", "precio": 80.00, "codigo": "RAY"},
    {"nombre": "Emergencia 24h", "precio": 100.00, "codigo": "EME"},
    {"nombre": "Hospitalización (día)", "precio": 60.00, "codigo": "HOS"}
]


def mostrar_catalogo_servicios():
    """
    Muestra el catálogo completo de servicios disponibles.
    Usa un arreglo (lista) para almacenar los servicios fijos.
    """
    print("\n    ╔════════════════════════════════════════════════════════════╗")
    print("    ║               💊 CATÁLOGO DE SERVICIOS                     ║")
    print("    ╠════════════════════════════════════════════════════════════╣")
    
    for i, servicio in enumerate(CATALOGO_SERVICIOS, 1):
        print(f"    ║  {i}. [{servicio['codigo']}] {servicio['nombre']:<20} ${servicio['precio']:.2f}")
    
    print("    ╚════════════════════════════════════════════════════════════╝")


def obtener_servicio(indice):
    """
    Obtiene un servicio del catálogo por su índice.
    
    Args:
        indice: Índice del servicio (1-indexado para el usuario)
    
    Returns:
        Diccionario con los datos del servicio, o None si no existe
    """
    if 1 <= indice <= len(CATALOGO_SERVICIOS):
        return CATALOGO_SERVICIOS[indice - 1]
    return None


# ==============================================================================
# SISTEMA PRINCIPAL - Clínica Veterinaria PET MARKET
# ==============================================================================
class SistemaVeterinaria:
    """
    Clase principal que integra todas las estructuras de datos
    para gestionar la clínica veterinaria.
    
    Componentes:
        - base_datos (ArbolBinario): Almacena todas las mascotas por ID
        - sala_espera (Cola): Gestiona el orden de atención de pacientes
    """
    
    def __init__(self):
        """
        Constructor del sistema.
        Inicializa el árbol de mascotas y la cola de espera.
        """
        self.base_datos = ArbolBinario()   # Árbol BST para mascotas
        self.sala_espera = Cola()          # Cola FIFO para sala de espera
    
    def inicializar_datos_prueba(self):
        """
        Carga datos de prueba para demostración del sistema.
        
        IMPORTANTE PARA LA EXPOSICIÓN:
        Esta función pre-carga mascotas, historial médico y cola de espera
        para poder demostrar todas las funcionalidades sin perder tiempo
        ingresando datos manualmente.
        """
        print("\n    ⏳ Cargando datos de prueba...")
        print("    " + "="*60)
        
        # ========== CREAR 5 MASCOTAS DE PRUEBA ==========
        mascota1 = Mascota(
            id=101,
            nombre="Max",
            raza="Golden Retriever",
            alergias="Ninguna conocida",
            nombre_dueno="Carlos Pérez",
            celular="0998-123-456"
        )
        
        mascota2 = Mascota(
            id=50,
            nombre="Luna",
            raza="Gato Siamés",
            alergias="Alergia a la penicilina",
            nombre_dueno="María García",
            celular="0987-654-321"
        )
        
        mascota3 = Mascota(
            id=150,
            nombre="Rocky",
            raza="Bulldog Francés",
            alergias="Sensibilidad a ciertos alimentos",
            nombre_dueno="Juan Rodríguez",
            celular="0976-111-222"
        )
        
        mascota4 = Mascota(
            id=75,
            nombre="Mía",
            raza="Poodle",
            alergias="Alergia a picaduras de pulgas",
            nombre_dueno="Ana Martínez",
            celular="0965-333-444"
        )
        
        mascota5 = Mascota(
            id=200,
            nombre="Thor",
            raza="Pastor Alemán",
            alergias="Ninguna conocida",
            nombre_dueno="Pedro Sánchez",
            celular="0954-555-666"
        )
        
        # ========== AGREGAR HISTORIAL MÉDICO PREVIO ==========
        # Max tiene 3 diagnósticos previos
        mascota1.agregar_diagnostico("15/09/2024 - Vacuna antirrábica anual aplicada")
        mascota1.agregar_diagnostico("20/10/2024 - Tratamiento para pulgas completado")
        mascota1.agregar_diagnostico("05/12/2024 - Consulta de rutina, todo bien")
        
        # Luna tiene 2 diagnósticos previos
        mascota2.agregar_diagnostico("10/08/2024 - Esterilización exitosa")
        mascota2.agregar_diagnostico("25/11/2024 - Control post-operatorio OK")
        
        # Rocky tiene 1 diagnóstico previo
        mascota3.agregar_diagnostico("01/12/2024 - Consulta por problemas digestivos")
        
        # Mía tiene 2 diagnósticos previos
        mascota4.agregar_diagnostico("18/07/2024 - Primer vacuna múltiple")
        mascota4.agregar_diagnostico("18/11/2024 - Refuerzo de vacunas")
        
        # Thor no tiene historial previo (nuevo paciente)
        
        # ========== INSERTAR EN EL ÁRBOL (BASE DE DATOS) ==========
        self.base_datos.insertar(mascota1)  # ID 101
        self.base_datos.insertar(mascota2)  # ID 50
        self.base_datos.insertar(mascota3)  # ID 150
        self.base_datos.insertar(mascota4)  # ID 75
        self.base_datos.insertar(mascota5)  # ID 200
        
        print("    ✅ 5 mascotas cargadas en la base de datos")
        print("    ✅ Historiales médicos cargados")
        
        # ========== AGREGAR 3 MASCOTAS A LA COLA DE ESPERA ==========
        self.sala_espera.encolar(mascota2)  # Luna - Primera en llegar
        self.sala_espera.encolar(mascota1)  # Max - Segundo
        self.sala_espera.encolar(mascota4)  # Mía - Tercera
        
        print("    ✅ 3 pacientes en sala de espera")
        print("    " + "="*60)
        print("    🎉 ¡Sistema listo para la demostración!")
    
    def mostrar_menu_principal(self):
        """
        Muestra el menú principal del sistema con todas las opciones disponibles.
        """
        print("\n")
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║                                                            ║")
        print("    ║     🐾  CLÍNICA VETERINARIA  🏥                            ║")
        print("    ║            ✨ PET MARKET ✨                                ║")
        print("    ║                                                            ║")
        print("    ╠════════════════════════════════════════════════════════════╣")
        print("    ║                                                            ║")
        print("    ║    1. 📝 Registrar Nueva Mascota                           ║")
        print("    ║    2. 🚶 Recepción (Agregar a Sala de Espera)              ║")
        print("    ║    3. 🩺 Atender Siguiente Paciente                        ║")
        print("    ║    4. 📋 Ver Historial Médico                              ║")
        print("    ║    5. 🗃️  Ver Base de Datos (Todas las Mascotas)           ║")
        print("    ║    6. 👥 Ver Sala de Espera                                ║")
        print("    ║    7. 💊 Ver Catálogo de Servicios                         ║")
        print("    ║    8. 🚪 Salir del Sistema                                 ║")
        print("    ║                                                            ║")
        print("    ╚════════════════════════════════════════════════════════════╝")
    
    def registrar_mascota(self):
        """
        Opción 1: Registra una nueva mascota en el sistema.
        
        Proceso:
            1. Solicitar todos los datos de la mascota
            2. Crear objeto Mascota
            3. Insertar en el Árbol Binario de Búsqueda
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("              📝 REGISTRO DE NUEVA MASCOTA")
        print("    ═══════════════════════════════════════════════════════════")
        
        try:
            # Solicitar ID único
            id_mascota = int(input("    🆔 Ingrese ID único de la mascota: "))
            
            # Verificar si el ID ya existe
            if self.base_datos.buscar(id_mascota) is not None:
                print("\n    ❌ ERROR: Ya existe una mascota con ese ID.")
                print("    Por favor, intente con un ID diferente.")
                return
            
            # Solicitar datos de la mascota
            nombre = input("    📛 Nombre de la mascota: ")
            raza = input("    🐕 Raza/Especie: ")
            alergias = input("    ⚠️  Alergias conocidas (o 'Ninguna'): ")
            nombre_dueno = input("    👤 Nombre del dueño: ")
            celular = input("    📱 Celular de contacto: ")
            
            # Crear y guardar la mascota
            nueva_mascota = Mascota(id_mascota, nombre, raza, alergias, nombre_dueno, celular)
            
            if self.base_datos.insertar(nueva_mascota):
                print("\n    ✅ ¡Mascota registrada exitosamente!")
                nueva_mascota.mostrar_informacion()
            else:
                print("\n    ❌ ERROR: No se pudo registrar la mascota.")
                
        except ValueError:
            print("\n    ❌ ERROR: El ID debe ser un número entero válido.")
    
    def recepcion_llegada(self):
        """
        Opción 2: Registra la llegada de una mascota a la sala de espera.
        
        Proceso:
            1. Buscar la mascota por ID en el Árbol
            2. Si existe, agregarla a la Cola de espera
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("             🚶 RECEPCIÓN - LLEGADA DE PACIENTE")
        print("    ═══════════════════════════════════════════════════════════")
        
        try:
            id_buscar = int(input("    🔍 Ingrese el ID de la mascota que llega: "))
            
            # Buscar en el árbol
            mascota = self.base_datos.buscar(id_buscar)
            
            if mascota is None:
                print("\n    ❌ ERROR: No se encontró una mascota con ese ID.")
                print("    💡 Sugerencia: Primero registre la mascota (Opción 1).")
                return
            
            # Agregar a la cola de espera
            self.sala_espera.encolar(mascota)
            
            print(f"\n    ✅ ¡{mascota.nombre} ha sido agregado(a) a la sala de espera!")
            print(f"    📍 Posición en la cola: {self.sala_espera.tamanio}")
            
            # Mostrar alergias importantes
            if mascota.alergias.lower() != "ninguna" and mascota.alergias.lower() != "ninguna conocida":
                print(f"    ⚠️  ATENCIÓN - Alergias: {mascota.alergias}")
                
        except ValueError:
            print("\n    ❌ ERROR: El ID debe ser un número entero válido.")
    
    def atender_paciente(self):
        """
        Opción 3: Atiende al siguiente paciente en la cola de espera.
        
        Proceso:
            1. Desencolar al primer paciente
            2. Mostrar su información
            3. Registrar un nuevo diagnóstico
            4. El diagnóstico se apila en el historial de la mascota
            5. Mostrar servicio y precio
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("                🩺 ATENCIÓN DE PACIENTE")
        print("    ═══════════════════════════════════════════════════════════")
        
        # Verificar si hay pacientes en espera
        if self.sala_espera.esta_vacia():
            print("\n    ℹ️  No hay pacientes en la sala de espera.")
            print("    💡 Use la opción 2 para registrar llegadas.")
            return
        
        # Desencolar al paciente
        mascota = self.sala_espera.desencolar()
        
        print(f"\n    📢 Llamando a: {mascota.nombre}")
        print("    " + "-"*50)
        mascota.mostrar_informacion()
        
        # Mostrar historial previo si existe
        if not mascota.historial_medico.esta_vacia():
            print("\n    📋 Último diagnóstico previo:")
            print(f"       {mascota.historial_medico.ver_tope()}")
        
        # Solicitar nuevo diagnóstico
        print("\n    " + "-"*50)
        diagnostico = input("    📝 Ingrese el diagnóstico de hoy: ")
        
        # Obtener fecha actual simulada (formato simple)
        from datetime import datetime
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        registro_completo = f"{fecha_actual} - {diagnostico}"
        
        # Apilar el diagnóstico en el historial
        mascota.agregar_diagnostico(registro_completo)
        
        print(f"\n    ✅ Diagnóstico registrado en el historial de {mascota.nombre}")
        
        # Seleccionar servicio prestado
        print("\n    💊 Seleccione el servicio prestado:")
        mostrar_catalogo_servicios()
        
        try:
            opcion_servicio = int(input("    Ingrese el número del servicio: "))
            servicio = obtener_servicio(opcion_servicio)
            
            if servicio:
                print("\n    ╔════════════════════════════════════════════════════════════╗")
                print("    ║                    💵 RESUMEN DE ATENCIÓN                  ║")
                print("    ╠════════════════════════════════════════════════════════════╣")
                print(f"    ║  🐾 Paciente:    {mascota.nombre}")
                print(f"    ║  💊 Servicio:    {servicio['nombre']}")
                print(f"    ║  💰 Total:       ${servicio['precio']:.2f}")
                print("    ╚════════════════════════════════════════════════════════════╝")
            else:
                print("    ⚠️  Servicio no encontrado, pero el diagnóstico fue guardado.")
                
        except ValueError:
            print("    ⚠️  Opción inválida, pero el diagnóstico fue guardado.")
        
        # Mostrar pacientes restantes
        if not self.sala_espera.esta_vacia():
            print(f"\n    👥 Quedan {self.sala_espera.tamanio} paciente(s) en espera.")
    
    def ver_historial(self):
        """
        Opción 4: Consulta el historial médico de una mascota.
        
        Proceso:
            1. Buscar la mascota por ID en el Árbol
            2. Mostrar su Pila de historial médico
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("              📋 CONSULTA DE HISTORIAL MÉDICO")
        print("    ═══════════════════════════════════════════════════════════")
        
        try:
            id_buscar = int(input("    🔍 Ingrese el ID de la mascota: "))
            
            # Buscar en el árbol
            mascota = self.base_datos.buscar(id_buscar)
            
            if mascota is None:
                print("\n    ❌ ERROR: No se encontró una mascota con ese ID.")
                return
            
            # Mostrar información básica y historial
            mascota.mostrar_informacion()
            mascota.ver_historial()
            
        except ValueError:
            print("\n    ❌ ERROR: El ID debe ser un número entero válido.")
    
    def ver_base_datos(self):
        """
        Opción 5: Muestra todas las mascotas registradas en el sistema.
        Usa el recorrido in-orden del Árbol Binario.
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("            🗃️  MASCOTAS REGISTRADAS EN EL SISTEMA")
        print("    ═══════════════════════════════════════════════════════════")
        
        self.base_datos.recorrido_inorden()
    
    def ver_sala_espera(self):
        """
        Opción 6: Muestra los pacientes en la sala de espera.
        """
        print("\n    ═══════════════════════════════════════════════════════════")
        print("                 👥 SALA DE ESPERA ACTUAL")
        print("    ═══════════════════════════════════════════════════════════")
        
        self.sala_espera.mostrar_sala_espera()
    
    def ejecutar(self):
        """
        Método principal que ejecuta el loop del menú interactivo.
        """
        print("\n")
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║                                                            ║")
        print("    ║    🏥 BIENVENIDO AL SISTEMA DE GESTIÓN VETERINARIA 🐾     ║")
        print("    ║                      PET MARKET                            ║")
        print("    ║                                                            ║")
        print("    ║          Sistema de Estructuras de Datos                   ║")
        print("    ║           Proyecto Final Universitario                     ║")
        print("    ║                                                            ║")
        print("    ╚════════════════════════════════════════════════════════════╝")
        
        # Cargar datos de prueba automáticamente
        self.inicializar_datos_prueba()
        
        # Loop principal del menú
        while True:
            self.mostrar_menu_principal()
            
            try:
                opcion = input("\n    ➤ Seleccione una opción (1-8): ").strip()
                
                if opcion == "1":
                    self.registrar_mascota()
                    
                elif opcion == "2":
                    self.recepcion_llegada()
                    
                elif opcion == "3":
                    self.atender_paciente()
                    
                elif opcion == "4":
                    self.ver_historial()
                    
                elif opcion == "5":
                    self.ver_base_datos()
                    
                elif opcion == "6":
                    self.ver_sala_espera()
                    
                elif opcion == "7":
                    mostrar_catalogo_servicios()
                    
                elif opcion == "8":
                    print("\n    " + "="*60)
                    print("    👋 ¡Gracias por usar PET MARKET!")
                    print("    🐾 Hasta pronto, que tengas un excelente día.")
                    print("    " + "="*60)
                    break
                    
                else:
                    print("\n    ⚠️  Opción no válida. Por favor, seleccione del 1 al 8.")
                    
            except Exception as e:
                print(f"\n    ❌ Error inesperado: {e}")
                print("    Por favor, intente nuevamente.")
            
            # Pausa para leer el resultado antes de mostrar el menú
            input("\n    ⏸️  Presione ENTER para continuar...")


# ==============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==============================================================================
if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Crea una instancia del sistema y lo ejecuta.
    """
    sistema = SistemaVeterinaria()
    sistema.ejecutar()
