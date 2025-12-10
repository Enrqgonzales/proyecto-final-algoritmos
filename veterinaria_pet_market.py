# Sistema de Gestión - Clínica Veterinaria "Pet Market"
# Proyecto Final - Estructuras de Datos

# Ancho fijo para todos los cuadros
ANCHO = 60


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.izquierdo = None
        self.derecho = None


class Pila:
    def __init__(self):
        self.tope = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.tope is None
    
    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamanio += 1
    
    def desapilar(self):
        if self.esta_vacia():
            return None
        
        dato_eliminado = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return dato_eliminado
    
    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.tope.dato
    
    def mostrar_historial(self):
        if self.esta_vacia():
            print("    No hay registros en el historial.")
            return
        
        actual = self.tope
        numero_registro = 1
        
        print(f"    ╔{'═' * ANCHO}╗")
        print(f"    ║{'HISTORIAL MÉDICO COMPLETO'.center(ANCHO)}║")
        print(f"    ╠{'═' * ANCHO}╣")
        
        while actual is not None:
            if numero_registro == 1:
                linea = f"> [{numero_registro}] {actual.dato}"
                print(f"    ║ {linea:<{ANCHO-2}} ║")
                print(f"    ║ {'(Más reciente)':<{ANCHO-2}} ║")
            else:
                linea = f"  [{numero_registro}] {actual.dato}"
                print(f"    ║ {linea:<{ANCHO-2}} ║")
            
            actual = actual.siguiente
            numero_registro += 1
        
        print(f"    ╚{'═' * ANCHO}╝")
        print(f"    Total de registros: {self.tamanio}")


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0
    
    def esta_vacia(self):
        return self.frente is None
    
    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        
        self.tamanio += 1
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        
        dato_eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        
        if self.frente is None:
            self.final = None
        
        self.tamanio -= 1
        return dato_eliminado
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.dato
    
    def mostrar_sala_espera(self):
        if self.esta_vacia():
            print("    La sala de espera está vacía.")
            return
        
        actual = self.frente
        posicion = 1
        
        print(f"    ╔{'═' * ANCHO}╗")
        print(f"    ║{'SALA DE ESPERA'.center(ANCHO)}║")
        print(f"    ╠{'═' * ANCHO}╣")
        
        while actual is not None:
            mascota = actual.dato
            if posicion == 1:
                linea = f"> Posición {posicion}: {mascota.nombre} (ID: {mascota.id})"
                print(f"    ║ {linea:<{ANCHO-2}} ║")
                print(f"    ║ {'(Siguiente en ser atendido)':<{ANCHO-2}} ║")
            else:
                linea = f"  Posición {posicion}: {mascota.nombre} (ID: {mascota.id})"
                print(f"    ║ {linea:<{ANCHO-2}} ║")
            
            actual = actual.siguiente
            posicion += 1
        
        print(f"    ╚{'═' * ANCHO}╝")
        print(f"    Total de pacientes en espera: {self.tamanio}")


class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0
    
    def esta_vacio(self):
        return self.raiz is None
    
    def insertar(self, mascota):
        nuevo_nodo = Nodo(mascota)
        
        if self.esta_vacio():
            self.raiz = nuevo_nodo
            self.cantidad += 1
            return True
        
        actual = self.raiz
        
        while True:
            if mascota.id < actual.dato.id:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    self.cantidad += 1
                    return True
                else:
                    actual = actual.izquierdo
            elif mascota.id > actual.dato.id:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    self.cantidad += 1
                    return True
                else:
                    actual = actual.derecho
            else:
                return False
    
    def buscar(self, id_mascota):
        actual = self.raiz
        
        while actual is not None:
            if id_mascota < actual.dato.id:
                actual = actual.izquierdo
            elif id_mascota > actual.dato.id:
                actual = actual.derecho
            else:
                return actual.dato
        
        return None
    
    def recorrido_inorden(self, nodo=None, primera_llamada=True):
        if primera_llamada:
            nodo = self.raiz
            if self.esta_vacio():
                print("    La base de datos está vacía.")
                return
            print(f"    ╔{'═' * ANCHO}╗")
            print(f"    ║{'BASE DE DATOS DE MASCOTAS'.center(ANCHO)}║")
            print(f"    ╠{'═' * ANCHO}╣")
        
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo, False)
            mascota = nodo.dato
            linea = f"ID: {mascota.id} | {mascota.nombre} | Dueño: {mascota.nombre_dueno}"
            print(f"    ║ {linea:<{ANCHO-2}} ║")
            self.recorrido_inorden(nodo.derecho, False)
        
        if primera_llamada:
            print(f"    ╚{'═' * ANCHO}╝")
            print(f"    Total de mascotas registradas: {self.cantidad}")


class Mascota:
    def __init__(self, id, nombre, raza, alergias, nombre_dueno, celular):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.alergias = alergias
        self.nombre_dueno = nombre_dueno
        self.celular = celular
        self.historial_medico = Pila()
    
    def mostrar_informacion(self):
        print(f"    ╔{'═' * ANCHO}╗")
        print(f"    ║{'FICHA DE LA MASCOTA'.center(ANCHO)}║")
        print(f"    ╠{'═' * ANCHO}╣")
        print(f"    ║ {'ID:':<18} {str(self.id):<{ANCHO-21}} ║")
        print(f"    ║ {'Nombre:':<18} {self.nombre:<{ANCHO-21}} ║")
        print(f"    ║ {'Raza:':<18} {self.raza:<{ANCHO-21}} ║")
        print(f"    ║ {'Alergias:':<18} {self.alergias:<{ANCHO-21}} ║")
        print(f"    ║ {'Dueño:':<18} {self.nombre_dueno:<{ANCHO-21}} ║")
        print(f"    ║ {'Celular:':<18} {self.celular:<{ANCHO-21}} ║")
        print(f"    ║ {'Registros:':<18} {str(self.historial_medico.tamanio) + ' diagnósticos':<{ANCHO-21}} ║")
        print(f"    ╚{'═' * ANCHO}╝")
    
    def agregar_diagnostico(self, diagnostico):
        self.historial_medico.apilar(diagnostico)
    
    def ver_historial(self):
        print(f"\n    Historial Médico de {self.nombre} (ID: {self.id}):")
        self.historial_medico.mostrar_historial()


# Catálogo de servicios
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
    print(f"\n    ╔{'═' * ANCHO}╗")
    print(f"    ║{'CATÁLOGO DE SERVICIOS'.center(ANCHO)}║")
    print(f"    ╠{'═' * ANCHO}╣")
    
    for i, servicio in enumerate(CATALOGO_SERVICIOS, 1):
        linea = f"{i}. [{servicio['codigo']}] {servicio['nombre']:<20} S/{servicio['precio']:.2f}"
        print(f"    ║ {linea:<{ANCHO-2}} ║")
    
    print(f"    ╚{'═' * ANCHO}╝")


def obtener_servicio(indice):
    if 1 <= indice <= len(CATALOGO_SERVICIOS):
        return CATALOGO_SERVICIOS[indice - 1]
    return None


class SistemaVeterinaria:
    def __init__(self):
        self.base_datos = ArbolBinario()
        self.sala_espera = Cola()
    
    def inicializar_datos_prueba(self):
        print("\n    Cargando datos de prueba...")
        print("    " + "="*ANCHO)
        
        # Crear mascotas de prueba
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
        
        # Agregar historial médico
        mascota1.agregar_diagnostico("15/09/2024 - Vacuna antirrábica anual aplicada")
        mascota1.agregar_diagnostico("20/10/2024 - Tratamiento para pulgas completado")
        mascota1.agregar_diagnostico("05/12/2024 - Consulta de rutina, todo bien")
        
        mascota2.agregar_diagnostico("10/08/2024 - Esterilización exitosa")
        mascota2.agregar_diagnostico("25/11/2024 - Control post-operatorio OK")
        
        mascota3.agregar_diagnostico("01/12/2024 - Consulta por problemas digestivos")
        
        mascota4.agregar_diagnostico("18/07/2024 - Primer vacuna múltiple")
        mascota4.agregar_diagnostico("18/11/2024 - Refuerzo de vacunas")
        
        # Insertar en el árbol
        self.base_datos.insertar(mascota1)
        self.base_datos.insertar(mascota2)
        self.base_datos.insertar(mascota3)
        self.base_datos.insertar(mascota4)
        self.base_datos.insertar(mascota5)
        
        print("    5 mascotas cargadas en la base de datos")
        print("    Historiales médicos cargados")
        
        # Agregar a la cola de espera
        self.sala_espera.encolar(mascota2)
        self.sala_espera.encolar(mascota1)
        self.sala_espera.encolar(mascota4)
        
        print("    3 pacientes en sala de espera")
        print("    " + "="*ANCHO)
        print("    Sistema listo!")
    
    def mostrar_menu_principal(self):
        print("\n")
        print(f"    ╔{'═' * ANCHO}╗")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ║{'CLÍNICA VETERINARIA'.center(ANCHO)}║")
        print(f"    ║{'PET MARKET'.center(ANCHO)}║")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ╠{'═' * ANCHO}╣")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ║ {'1. Registrar Nueva Mascota':<{ANCHO-2}} ║")
        print(f"    ║ {'2. Recepción (Agregar a Sala de Espera)':<{ANCHO-2}} ║")
        print(f"    ║ {'3. Atender Siguiente Paciente':<{ANCHO-2}} ║")
        print(f"    ║ {'4. Ver Historial Médico':<{ANCHO-2}} ║")
        print(f"    ║ {'5. Ver Base de Datos (Todas las Mascotas)':<{ANCHO-2}} ║")
        print(f"    ║ {'6. Ver Sala de Espera':<{ANCHO-2}} ║")
        print(f"    ║ {'7. Ver Catálogo de Servicios':<{ANCHO-2}} ║")
        print(f"    ║ {'8. Salir del Sistema':<{ANCHO-2}} ║")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ╚{'═' * ANCHO}╝")
    
    def registrar_mascota(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'REGISTRO DE NUEVA MASCOTA'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        try:
            id_mascota = int(input("    Ingrese ID único de la mascota: "))
            
            # Validar ID
            if self.base_datos.buscar(id_mascota) is not None:
                print("\n    Ya existe una mascota con ese ID.")
                print("    Intente con un ID diferente.")
                return
            
            nombre = input("    Nombre de la mascota: ")
            raza = input("    Raza/Especie: ")
            alergias = input("    Alergias conocidas (o 'Ninguna'): ")
            nombre_dueno = input("    Nombre del dueño: ")
            celular = input("    Celular de contacto: ")
            
            nueva_mascota = Mascota(id_mascota, nombre, raza, alergias, nombre_dueno, celular)
            
            if self.base_datos.insertar(nueva_mascota):
                print("\n    Mascota registrada correctamente!")
                nueva_mascota.mostrar_informacion()
            else:
                print("\n    No se pudo registrar la mascota.")
                
        except ValueError:
            print("\n    El ID debe ser un número entero.")
    
    def recepcion_llegada(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'RECEPCIÓN - LLEGADA DE PACIENTE'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        try:
            id_buscar = int(input("    Ingrese el ID de la mascota que llega: "))
            
            mascota = self.base_datos.buscar(id_buscar)
            
            if mascota is None:
                print("\n    No se encontró una mascota con ese ID.")
                print("    Primero registre la mascota (Opción 1).")
                return
            
            self.sala_espera.encolar(mascota)
            
            print(f"\n    {mascota.nombre} agregado(a) a la sala de espera!")
            print(f"    Posición en la cola: {self.sala_espera.tamanio}")
            
            if mascota.alergias.lower() != "ninguna" and mascota.alergias.lower() != "ninguna conocida":
                print(f"    Alergias: {mascota.alergias}")
                
        except ValueError:
            print("\n    El ID debe ser un número entero.")
    
    def atender_paciente(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'ATENCIÓN DE PACIENTE'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        if self.sala_espera.esta_vacia():
            print("\n    No hay pacientes en la sala de espera.")
            print("    Use la opción 2 para registrar llegadas.")
            return
        
        mascota = self.sala_espera.desencolar()
        
        print(f"\n    Llamando a: {mascota.nombre}")
        print("    " + "-"*50)
        mascota.mostrar_informacion()
        
        if not mascota.historial_medico.esta_vacia():
            print("\n    Último diagnóstico previo:")
            print(f"       {mascota.historial_medico.ver_tope()}")
        
        print("\n    " + "-"*50)
        diagnostico = input("    Ingrese el diagnóstico de hoy: ")
        
        from datetime import datetime
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        registro_completo = f"{fecha_actual} - {diagnostico}"
        
        mascota.agregar_diagnostico(registro_completo)
        
        print(f"\n    Diagnóstico registrado en el historial de {mascota.nombre}")
        
        print("\n    Seleccione el servicio prestado:")
        mostrar_catalogo_servicios()
        
        try:
            opcion_servicio = int(input("    Ingrese el número del servicio: "))
            servicio = obtener_servicio(opcion_servicio)
            
            if servicio:
                print(f"\n    ╔{'═' * ANCHO}╗")
                print(f"    ║{'RESUMEN DE ATENCIÓN'.center(ANCHO)}║")
                print(f"    ╠{'═' * ANCHO}╣")
                print(f"    ║ {'Paciente:':<15} {mascota.nombre:<{ANCHO-18}} ║")
                print(f"    ║ {'Servicio:':<15} {servicio['nombre']:<{ANCHO-18}} ║")
                print(f"    ║ {'Total:':<15} {'S/' + str(servicio['precio']):<{ANCHO-18}} ║")
                print(f"    ╚{'═' * ANCHO}╝")
            else:
                print("    Servicio no encontrado, pero el diagnóstico fue guardado.")
                
        except ValueError:
            print("    Opción inválida, pero el diagnóstico fue guardado.")
        
        if not self.sala_espera.esta_vacia():
            print(f"\n    Quedan {self.sala_espera.tamanio} paciente(s) en espera.")
    
    def ver_historial(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'CONSULTA DE HISTORIAL MÉDICO'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        try:
            id_buscar = int(input("    Ingrese el ID de la mascota: "))
            
            mascota = self.base_datos.buscar(id_buscar)
            
            if mascota is None:
                print("\n    No se encontró una mascota con ese ID.")
                return
            
            mascota.mostrar_informacion()
            mascota.ver_historial()
            
        except ValueError:
            print("\n    El ID debe ser un número entero.")
    
    def ver_base_datos(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'MASCOTAS REGISTRADAS EN EL SISTEMA'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        self.base_datos.recorrido_inorden()
    
    def ver_sala_espera(self):
        print("\n    " + "═"*ANCHO)
        print(f"{'SALA DE ESPERA ACTUAL'.center(ANCHO + 4)}")
        print("    " + "═"*ANCHO)
        
        self.sala_espera.mostrar_sala_espera()
    
    def ejecutar(self):
        print("\n")
        print(f"    ╔{'═' * ANCHO}╗")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ║{'BIENVENIDO AL SISTEMA DE GESTIÓN VETERINARIA'.center(ANCHO)}║")
        print(f"    ║{'PET MARKET'.center(ANCHO)}║")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ║{'Sistema de Estructuras de Datos'.center(ANCHO)}║")
        print(f"    ║{'Proyecto Final Universitario'.center(ANCHO)}║")
        print(f"    ║{' ' * ANCHO}║")
        print(f"    ╚{'═' * ANCHO}╝")
        
        self.inicializar_datos_prueba()
        
        # Bucle principal
        while True:
            self.mostrar_menu_principal()
            
            try:
                opcion = input("\n    Seleccione una opción (1-8): ").strip()
                
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
                    print("\n    " + "="*ANCHO)
                    print("    Gracias por usar PET MARKET!")
                    print("    Hasta pronto.")
                    print("    " + "="*ANCHO)
                    break
                    
                else:
                    print("\n    Opción no válida. Seleccione del 1 al 8.")
                    
            except Exception as e:
                print(f"\n    Error: {e}")
            
            input("\n    Presione ENTER para continuar...")


if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.ejecutar()
