from django.shortcuts import render
from django.http import HttpResponse
from item.models import Item, Category


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',
                  {
                      'categories': categories,
                      'items': items,
                  })


def checkout(request):
    return HttpResponse('this is checkout page')
