class Array:
    def __init__(self, tam):
        self.__info = [0 for x in range(tam)]

    def get_item(self, posicion):
        return self.__info[posicion]
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("Error de posicion")
        return dato

    def set_item(self, dato ,posicion):
        try:
            self.__info[posicion] = dato
        except Exception as e:
            print("Error de posicion")

    def get_length(self):
        return len(self.__info)

algo = Array(10)
print(algo.get_item(6363))
algo.set_item()
print(algo.get_item(3))
print(f"El arreglo tiene{algo.get_length()} elementos")
