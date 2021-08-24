class Bebe:
    def __init__(self, nome, mae = None):
        if (mae is None):
            print("Bebê depende de mãe, não posso instanciar essa criança")
            return

        self.__nome = nome

    def get_nome(self):
        return self.__nome