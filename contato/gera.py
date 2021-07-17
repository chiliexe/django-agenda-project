
from random import randint

data = ["Ad\u00e3o Uchoa", "Amadeu P\u00e1dua", "Am\u00e9rico Couto", "Angelino Alburquerque", "Anind Santiago",
        "Ant\u00f3nia Soares", "Brites Puentes", "Catarina Silveira", "Claudemira Ventura", "Dinis Guaran\u00e1",
        "Emanuel Raminhos", "Estanislau Vargas", "Eurico Parente", "Evaristo Passos", "Fabiana Belchiorinho",
        "Filipe Trist\u00e3o", "Frederica Cayado", "Guterre Leit\u00e3o", "Helo\u00edsa Macedo",
        "Herculano Gouveia", "H\u00e9lio Guedez", "Ilma Botica", "Israel Ignacio", "Janda\u00edra Palma",
        "Juliano Telles", "Ju\u00e7ara Valent\u00edn", "Leopoldina Andrade", "Luciano Caldas",
        "L\u00facia Vergueiro", "Margarida Nascimento", "Miru Brum", "M\u00e1ximo Trinidad", "Neusa Lemes",
        "Nivaldo Mata", "Oliveira Briones", "Pandora Brum", "Pen\u00e9lope Cordero", "Roberto Alvarenga",
        "Rodolfo Souza", "Rudi Paranhos", "Son\u00e1s Guedes", "Son\u00e1s Guzm\u00e1n",
        "Suni\u00e1rio Rem\u00edgio", "Tabalipa Carmona", "Tairine Anhaia", "Tobias Fartaria",
        "Ubirat\u00e3 Guar\u00e1", "Ulrico Ornellas", "Vanessa Murici", "V\u00e2nia Sarmiento"]

ddd = str(randint(1, 9)) + str(randint(0, 9))
digitos1 = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
digitos2 = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
full = f"({ddd}) {digitos1} - {digitos2}"

categoria = randint(1, 5)
print(digitos1)