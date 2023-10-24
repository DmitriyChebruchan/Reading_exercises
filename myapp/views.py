from django.shortcuts import render
from .models import UserInput


def index(request):
    return render(request, 'myapp/index.html')


def submit(request):
    if request.method == 'POST':
        text = request.POST['text']
        speed = request.POST['speed']

        user_input = UserInput(text=text, speed=speed)

        user_input.save()
        return render(request, 'myapp/display.html', {'user_input': user_input})
