from django.shortcuts import render

# Create your views here.
def index(request):
    productos = [
        {"nombre": "Laptop Pro X", "precio": 1200, "disponible": True},
        {"nombre": "Teclado Mecánico RGB", "precio": 90, "disponible": False},
        {"nombre": "Mouse Ergonómico Inalámbrico", "precio": 50, "disponible": True},
    ]
    contexto = {
        'nombre_negocio': 'TecnoEmpresa S.A.',
        'productos': productos
    }
    return render(request, 'index.html', contexto)
