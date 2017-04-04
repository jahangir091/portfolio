

from django.shortcuts import get_object_or_404, render


def detail(request):
    return render(request, 'index.html')

def birthday(request):
    return render(request, 'birthday.html')