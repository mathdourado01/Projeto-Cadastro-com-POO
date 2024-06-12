from model.restaurante import Restaurante

restaurante1 = Restaurante("praca","Italiana")
#restaurante1.receber_avaliacao("Gui", 5)
#restaurante1.receber_avaliacao("mAthi", 0)
#restaurante2 = Restaurante("pizza Express", "Italiana")
#restaurante3 = Restaurante("Mexicano Maluco", "Mexicano")
def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()