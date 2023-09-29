from django.shortcuts import render
from .models import Item, Category
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def details(request, pk):
    item = Item.objects.get(pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    return render(request, 'item/details.html',{
        'item': item,
        'related_items': related_items
    })


def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if len(items) == 0:
        messages.info(request, "No search item here")

    return render(request, 'core/index.html', {
        'items': items,

    })
