from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        character = request.POST['data']
        data = {}
        res = requests.get('https://superheroapi.com/api.php/232593295392235/search/' + character).json()

       

        

        

        return render(request, 'index.html', {'res': res} )
    else:
        return render(request, 'index.html')
