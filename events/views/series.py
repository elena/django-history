# -*- coding: utf-8 -*-
from django.views import generic
from ..models import Series


class QuerySetMixin(object):

    model = Series


class DetailView(QuerySetMixin, generic.DetailView):

    pass


class ListView(QuerySetMixin, generic.ListView):

    pass