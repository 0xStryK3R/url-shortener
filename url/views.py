import random
import string
from django.shortcuts import render, redirect

from url.models import UrlData
from .forms import UrlForm


def urlShort(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            #request.user.urlshort.add(new_url)
            #return redirect('/')
    else:
        form = UrlForm()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'url\index.html', context)