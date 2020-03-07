import datetime

from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.urls import reverse

from yaurl.forms import ShortedUrlForm
from yaurl.models import ShortedUrl


def index(req):
    shorted_url_form = ShortedUrlForm()
    available_shorts = ShortedUrl.objects.all()
    return render(req, 'yaurl/index.html', {
        'shorted_url_form': shorted_url_form,
        'shorted_urls': sorted(available_shorts,
                               key=lambda short: short.created_at,
                               reverse=True),
    })


def add(req):
    form = ShortedUrlForm(req.POST)
    if form.is_valid():
        new_shorted_url = ShortedUrl(
            original_url=form.cleaned_data['original_url'],
            created_at=datetime.datetime.now())
        new_shorted_url.save()
    return redirect(reverse('index'))


def shorted_url_redirect(req, shorted_id):
    shorted_url = get_object_or_404(ShortedUrl, pk=shorted_id)
    shorted_url.redirects = F('redirects') + 1
    shorted_url.save()
    return redirect(shorted_url.original_url)
