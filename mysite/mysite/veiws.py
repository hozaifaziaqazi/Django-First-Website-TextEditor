# I created the file
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('''<h1>Hello World, I am Hozaifa and I am CEO of Google, Amazon and  Microsoft</h1>
     <a href="https://www.youtube.com/channel/UCB7LRgiNiGniUb5SKG81C-g">Rambling Kids Youtube Chanel</a> <br>
     <a href="http://127.0.0.1:8000">Home</a> <br>
     <a href="http://127.0.0.1:8000/index/">Index</a> <br>
     <a href="http://127.0.0.1:8000/about/">About</a> <br> ''')


def index(request):
    a = {'Name': 'Hozaifa', 'Age': '13', 'Place': 'Pakistan'}
    return render(request, 'index.html', a)


def about(request):
    return HttpResponse('''<h3>Hello World, I am Hozaifa Zia</h3> <a href="https://www.google.com/">Google</a> 
    <br> <a href="http://127.0.0.1:8000">Home</a> <br> ''')








