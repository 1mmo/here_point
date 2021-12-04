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
        q = Q(title__icontains=keyword) | Q(content__incontains=keyword)
        places = places.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(places, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"category": category, "page": page, 
               "places": page.object_list, "form": form}
    return render(request, 'by_category.html', context)
