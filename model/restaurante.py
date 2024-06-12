from model.avaliacao import Avaliacao
    
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self.nome} | {self.categoria}" 
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome} |  {restaurante.categoria} | {restaurante.ativo} | {restaurante.media_avaliacoes}")
    
    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Desativado"
    
    def alterar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self,cliente, nota):
        avaliacoes = Avaliacao(cliente,nota)
        if nota > 5:
            print("Nota mais alta do que pode!")
        else:
            self._avaliacao.append(avaliacoes)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Sem avaliação"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas,1)
        return media

