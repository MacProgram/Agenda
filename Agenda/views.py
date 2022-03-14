from django.http import HttpResponse
from django.template import Template, Context

def Mostrar(request):
    DoxOut = open(r"D:/Users/lukym/Desktop/Projects/CasillaComentario/static/index.html")
    plt = Template(DoxOut.read())
    DoxOut.close()

    pris = open(r"D:/Users/lukym/Desktop/Projects/CasillaComentario/static/styler.css")
    ctx = Context(pris.read())
    Doc = plt.render(ctx)

    return HttpResponse(Doc)
