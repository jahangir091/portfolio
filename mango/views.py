from django.shortcuts import render
from django.views.generic.list import ListView

from mango.models import Mango


class MangoListView(ListView):
    """
    This view lists all the slider images
    """
    template_name = 'mango_list.html'
    model = Mango

    def get_queryset(self):
        return Mango.objects.all().order_by('-date_created')[:15]