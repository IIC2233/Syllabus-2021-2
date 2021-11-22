from collections import deque

class Empresa:
    
    def __init__(self, id_colaborador, nombre, tiempo_servicio, sueldo, jefe=None):
        self.id_colaborador = id_colaborador
        self.jefe = jefe
        self.nombre = nombre
        self.tiempo_servicio = tiempo_servicio
        self.sueldo = sueldo
        self.hijos = {}
        
    def obtener_nodo(self, id_colaborador):
        
        # Vemos si es el mimso
        if self.id_colaborador == id_colaborador:
            return self
        
        # Buscamos en los hijos recursivamente, hasta encontrar el mismo
        for hijo in self.hijos.values():
            nodo_obtenido = hijo.obtener_nodo(id_colaborador)
            if nodo_obtenido is not None:
                return nodo_obtenido
            
    def agregar_nodo(self, id_jefe, id_colaborador, nombre, tiempo_servicio, sueldo):
        jefe = self.obtener_nodo(id_jefe)
        
        if jefe is None:
            return
        
        colaborador = Empresa(id_colaborador, nombre, tiempo_servicio, sueldo, jefe)
        jefe.hijos[id_colaborador] = colaborador
        
    def soy_nuevo(self):
        
        if not self.hijos and self.tiempo_servicio < 2:
            self.sueldo = self.sueldo * 0.1
            return True
        return False
            
    def jerarquia(self, id_colaborador):
        colaborador = self.obtener_nodo(id_colaborador)
        return colaborador.jefes()
    
    def jefes(self):
        if not self.jefe:
            return [self.nombre]
        
        lista_jefes = self.jefe.jefes()
        lista_jefes.append(self.nombre)
        
        return lista_jefes
    
    def mas_nuevo_bfs(self):
        """Método que recorre el arbol utilizando BFS, con la condición de que al encontrar
        una persona nueva se termine el recorrido"""

        # Utilizamos el mismo método visto en clases
        cola = deque()
        cola.append(self)
        while len(cola) > 0:
            nodo_actual = cola.popleft()
            yield nodo_actual
            # En el caso de que el nodo actual cumpla las condiciones, terminamos el recorrido
            if nodo_actual.soy_nuevo():
                break
            for hijo in nodo_actual.hijos.values():
                cola.append(hijo)
    
    def mas_nuevo_dfs(self):
        """Método que recorre el arbol utilizando DFS, con la condición de que al encontrar
        a una persona nueva se termine el recorrido"""

        yield self
        # Despues de devolver el nodo en la iteración, revisamos si el nodo cumple la condición. Si
        # es que se cumple, retornamos True.
        if self.soy_nuevo():
            return True
        for subarbol in self.hijos.values():
            # El valor de la variable encontrado será None hasta que se encuentre un nodo indicado.
            # En ese caso, se devuelve True en todas las subrutinas, terminandolas.
            encontrado = yield from subarbol.mas_nuevo_dfs()
            if encontrado:
                return True

empresa = Empresa(0, "Carla", 15, 100)
empresa.agregar_nodo(0, 1, "James", 10, 90)
empresa.agregar_nodo(0, 2, "Juanita", 8, 94)
empresa.agregar_nodo(0, 3, "Carlos", 9, 92)
empresa.agregar_nodo(1, 4, "Maca", 5, 60)
empresa.agregar_nodo(1, 5, "Antonia", 6, 63)
empresa.agregar_nodo(2, 6, "José", 7, 67)
empresa.agregar_nodo(2, 7, "Esteban", 4, 45)
empresa.agregar_nodo(3, 8, "Tere", 3, 44)
empresa.agregar_nodo(3, 9, "Pablo", 1, 41)

print(empresa.jerarquia(9))
print(30 * "-")
print("Busqueda DFS")
for i in empresa.mas_nuevo_dfs():
    print(f"{i.nombre} -> {i.id_colaborador}")
print("")
print(30 * "-")
print("Busqueda BFS")
for i in empresa.mas_nuevo_bfs():
    print(f"{i.nombre} -> {i.id_colaborador}")
