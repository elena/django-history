# -*- coding: utf-8 -*-
from django.views import generic
from ..models import Talk


class QuerySetMixin(object):

    model = Talk


class DetailView(QuerySetMixin, generic.DetailView):

    pass


class ListView(QuerySetMixin, generic.ListView):

    pass