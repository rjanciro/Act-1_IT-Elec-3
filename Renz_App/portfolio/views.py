from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'pages/portfolio.html', context)

