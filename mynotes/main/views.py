from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'title': 'Главная страница',
            'values': ['some text', 'some hello', 'some world']
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

