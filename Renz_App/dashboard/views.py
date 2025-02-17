from django.shortcuts import render

# Create your views here.

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    
    context = {
        'title': 'Dashboard',
        'user': 'Renz',
        'cards': data
    }
    return render(request, 'pages/dashboard.html', context)
