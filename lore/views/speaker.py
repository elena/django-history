# -*- coding: utf-8 -*-
from django.views import generic
from ..models import Speaker


class QuerySetMixin(object):

    model = Speaker


class DetailView(QuerySetMixin, generic.DetailView):

    pass


class ListView(QuerySetMixin, generic.ListView):

    pass