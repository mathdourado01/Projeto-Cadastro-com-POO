from model.restaurante import Restaurante
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato
from sobremesa import Sobremesa
restaurante1 = Restaurante("praca","Italiana")
bebidas = Bebida('Suco de Melancia', 5, 'grande')
prato1 = Prato('Pao', 2, 'Melhor pão da cidade')
sobremesa = Sobremesa("Musse",10,"Chocolate","Grande")
bebidas.aplicar_desconto()
prato1.aplicar_desconto()
sobremesa.aplicar_desconto()
restaurante1.adicionar_no_cardapio(bebidas)
restaurante1.adicionar_no_cardapio(prato1)
restaurante1.adicionar_no_cardapio(sobremesa)


def main():
    restaurante1.exibir_cardapio
if __name__ == '__main__':
    main()