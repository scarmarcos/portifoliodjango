from django.shortcuts import render

def portfolio_exibir(request):
    return render(request, 'portfolio/portfolio_exibir.html', {})
