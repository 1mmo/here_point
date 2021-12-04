from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Category, Place
from .forms import SearchForm


def by_category(request, pk):
    """ Get category from user's request """
    category = get_object_or_404(Category, pk=pk)
    places = Place.objects.filter(is_active=True, categories=pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword)
        places = places.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(places, 10)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"category": category, "page": page, 
               "places": page.object_list, "form": form}
    return render(request, 'by_category.html', context)

def detail(request, category_pk, pk):
    place = get_object_or_404(Place, pk=pk)
    ais = place.additionalimage_set.all()
    context = {'place': place, 'ais': ais}
    return render(request, 'detail.html', context)

def index(request):
    return render(request, 'primary_main.html')
