class No:
    def __init__(self, nome:str,  funcaoH:float):
        self.nome = nome
        self.funcaoH = funcaoH
        self.funcaoF = 0
        self.funcaoG = 0
        self.no_antecessor = None
        self.adjacentes = []

    def get_nome(self):
        return self.nome
    def get_funcaoH(self):
        return self.funcaoH
    def get_funcaoF(self):
        return self.funcaoF
    def get_funcaoG(self):
        return self.funcaoG
    def get_no_antecessor(self):
        return self.no_antecessor
    def get_adjacentes(self):
        return self.adjacentes


    def set_funcaoG(self, funcaoG:float):
        self.funcaoG = funcaoG
    def set_funcaoF(self, funcaoF:float):
        self.funcaoF = funcaoF
    def set_adjasente(self, adjacentes:list):
        self.adjacentes = adjacentes
    def set_no_antecessor(self, no_antecessor):
        self.no_antecessor = no_antecessor