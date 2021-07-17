from django.views import generic
from .models import Contato, Category
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.db.models import Q, Value
from django.db.models.functions import Concat

# def gera():
#     data = ["Ad\u00e3o Uchoa", "Amadeu P\u00e1dua", "Am\u00e9rico Couto", "Angelino Alburquerque", "Anind Santiago",
#             "Ant\u00f3nia Soares", "Brites Puentes", "Catarina Silveira", "Claudemira Ventura", "Dinis Guaran\u00e1",
#             "Emanuel Raminhos", "Estanislau Vargas", "Eurico Parente", "Evaristo Passos", "Fabiana Belchiorinho",
#             "Filipe Trist\u00e3o", "Frederica Cayado", "Guterre Leit\u00e3o", "Helo\u00edsa Macedo",
#             "Herculano Gouveia", "H\u00e9lio Guedez", "Ilma Botica", "Israel Ignacio", "Janda\u00edra Palma",
#             "Juliano Telles", "Ju\u00e7ara Valent\u00edn", "Leopoldina Andrade", "Luciano Caldas",
#             "L\u00facia Vergueiro", "Margarida Nascimento", "Miru Brum", "M\u00e1ximo Trinidad", "Neusa Lemes",
#             "Nivaldo Mata", "Oliveira Briones", "Pandora Brum", "Pen\u00e9lope Cordero", "Roberto Alvarenga",
#             "Rodolfo Souza", "Rudi Paranhos", "Son\u00e1s Guedes", "Son\u00e1s Guzm\u00e1n",
#             "Suni\u00e1rio Rem\u00edgio", "Tabalipa Carmona", "Tairine Anhaia", "Tobias Fartaria",
#             "Ubirat\u00e3 Guar\u00e1", "Ulrico Ornellas", "Vanessa Murici", "V\u00e2nia Sarmiento"]
#
#     for d in data:
#         ddd = str(randint(1, 9)) + str(randint(0, 9))
#         digitos1 = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
#         digitos2 = str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9)) + str(randint(1, 9))
#         telefone = f"({ddd}) {digitos1} - {digitos2}"
#         fullname = d.split(" ")
#         name = fullname[0]
#         lastname = fullname[1]
#         category = Category.objects.get(pk=randint(1, 5))
#         newcontato = Contato(name=name, last_name=lastname, phone=telefone, category=category)
#         newcontato.save()


class ContatoListView(generic.ListView):
    template_name = "contato/index.html"
    model = Contato
    context_object_name = 'contatos'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        full_name = Concat('name', Value(' '), 'last_name')
        query = self.request.GET.get('query')
        if query:
            qs = qs.annotate(full_name=full_name)\
                .filter(Q(full_name__contains=query) | Q(phone__contains=query))
        else:
            qs = qs.order_by('-id')
        return qs


class ContatoDetailView(generic.DetailView):
    model = Contato
    template_name = "contato/detail.html"
    context_object_name = 'contato'


class ContatoCreateView(generic.CreateView):
    model = Contato
    template_name = "contato/create.html"
    form_class = ContatoForm
    success_url = reverse_lazy('home:index')

