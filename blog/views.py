from django.shortcuts import render

def index(request):
    data = {'mydata' : "Hello World"}
    return render(request, 'blog/index.html', data)
