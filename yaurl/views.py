from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.urls import reverse
from django.utils import timezone

from yaurl.forms import ShortedUrlForm, RemoveShortedUrlForm
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


@login_required()
def add(req):
    form = ShortedUrlForm(req.POST)
    if form.is_valid():
        new_shorted_url = ShortedUrl(
            original_url=form.cleaned_data['original_url'],
            created_at=timezone.now(),
            user=req.user)
        new_shorted_url.save()
    return redirect(reverse('index'))


@login_required()
def remove(req):
    form = RemoveShortedUrlForm(req.POST)
    if form.is_valid():
        short = get_object_or_404(ShortedUrl, pk=form.cleaned_data['shorted_id'])
        if short.user != req.user:
            return HttpResponseForbidden('!')
        short.delete()
    return redirect(reverse('profile'))


def shorted_url_redirect(req, shorted_id):
    shorted_url = get_object_or_404(ShortedUrl, pk=shorted_id)
    shorted_url.redirects = F('redirects') + 1
    shorted_url.save()
    return redirect(shorted_url.original_url)
