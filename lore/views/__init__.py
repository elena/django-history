# -*- coding: utf-8 -*-
from django.views import generic
from ..models import Talk


class HomePageView(generic.ListView):

    model = Talk
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super(HomePageView, self).get_context_data(*args, **kwargs)
        context_data.update({
            # 'popular': self.form,
            # 'recent': self.request.GET.urlencode(),
            # 'unwatched': self.get_person()
        })
        return context_data
