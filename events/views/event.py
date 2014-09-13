# -*- coding: utf-8 -*-
from django.views import generic
from ..models import Event

class QuerySetMixin(object):

    model = Event

    def get_queryset(self, *args, **kwargs):
        queryset = super(QuerySetMixin, self).get_queryset(*args, **kwargs)

        ## TD: active() queryset and object pass through manager.
        return queryset.filter(is_live=True)


class DetailView(QuerySetMixin, generic.DetailView):

    pass


class ListView(QuerySetMixin, generic.ListView):

    pass