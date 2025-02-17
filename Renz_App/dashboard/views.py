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

def reports(request):
    reports_data = [
        {"name": "Sales Report", "period": "Monthly", "last_updated": "2024-02-17"},
        {"name": "User Activity", "period": "Weekly", "last_updated": "2024-02-15"},
        {"name": "Revenue Analysis", "period": "Quarterly", "last_updated": "2024-02-01"},
    ]
    context = {
        'title': 'Reports',
        'user': 'Renz',
        'reports': reports_data
    }
    return render(request, 'pages/reports.html', context)

def settings(request):
    settings_data = {
        'profile': {
            'name': 'Renz',
            'email': 'renz@example.com',
            'role': 'Administrator'
        },
        'preferences': {
            'theme': 'Light',
            'notifications': 'Enabled',
            'language': 'English'
        }
    }
    context = {
        'title': 'Settings',
        'user': 'Renz',
        'settings': settings_data
    }
    return render(request, 'pages/settings.html', context)
