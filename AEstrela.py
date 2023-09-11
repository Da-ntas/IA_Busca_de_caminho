from no import *

class AEstrela:
    def menor_funcao_f(self, prioridades):
        no_menor_custo = prioridades[0]
        for no_atual in prioridades:
            if no_menor_custo.get_funcaoF() < no_menor_custo.get_funcaoF():
                no_menor_custo = no_atual
        prioridades.remove(no_menor_custo)
        return no_menor_custo
    def busca_AEstrela(self, no_origem:No, no_destino:No):
        #criar as filas vazias
        prioridades=[]
        explorados=[]

        #se origem == destino finaliza
        if no_origem != no_destino:
            #fila Prioridade adiciona origem
            prioridades.append(no_origem)
            #Enquanto fila prioridade nao vazia e destino nao encontrado
            no_atual = prioridades[0]
            while len(prioridades)>0 and (no_atual != no_destino):
                #FIla explorados adiciona nó atual
                explorados.append(no_atual)
                #Se no atual == destino -> parar
                #Para cada aresta adjacente do no atual
                for arestas in no_atual.get_adjacentes():
                    # No filho = aresta.alvo
                    no_filho = arestas.get_no_alvo()
                    g_temp = no_atual.get_funcaoG() + arestas.get_custo()
                    f_temp = g_temp + no_filho.get_funcaoH()
                    # Se caso o nó filho ja tenha sido explorado
                    # e seu valor de funcao f é maior que a funcao f do pai,
                    # entao ele e desconsiderado
                    if not(no_filho in explorados and f_temp > no_atual.get_funcaoF()):
                        # senão se o nó filho nao esta na filaPrioridade ou sua funcao f é maior que a funcao ftemp
                        if no_filho not in prioridades or no_filho.get_funcaoF() > f_temp:
                            no_filho.set_no_antecessor(no_atual)
                            no_filho.set_funcaoG(g_temp)
                            no_filho.set_funcaoF(f_temp)
                            prioridades.append(no_filho)
                # No atual = no com menor funcao f
                no_atual = self.menor_funcao_f(prioridades)


    def percorrer_caminho(self, alvo:No):
        caminho =']'
        while not (alvo is None):
            caminho = ', ' + alvo.get_nome() + caminho
            alvo = alvo.get_no_antecessor()
        caminho = '['+caminho
        return caminho