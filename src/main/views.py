from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Category, Place, Comment
from .forms import SearchForm, UserCommentForm, GuestCommentForm


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
    """ Displaying information about place """
    place = get_object_or_404(Place, pk=pk)
    ais = place.additionalimage_set.all()
    comments = Comment.objects.filter(place=pk, is_active=True)
    initial = {'place': place.pk}
    if request.user.is_authenticated:
        initial['author'] = request.user.username
        form_class = UserCommentForm
    else:
        form_class = GuestCommentForm
    form = form_class(initial=initial)
    if request.method == "POST":
        c_form = form_class(request.POST)
        if c_form.is_valid():
            c_form.save()
        else:
            form = c_form
    category = place.categories.all()
    context = {'place': place, 'ais': ais, 'category': category,
               'comments': comments, 'form': form}
    #if request.user.username:
    #    author = request.user.username
    #    context['author'] = author
    return render(request, 'detail.html', context)

def index(request):
    places = Place.objects.filter(is_active=True)[:10]
    context = {'places': places}
    return render(request, 'primary_main.html', context)
