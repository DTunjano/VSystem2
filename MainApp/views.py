from django.shortcuts import render # type: ignore

def paginaPrincipal(request):
    return render(request, 'index.html')
