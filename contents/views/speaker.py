# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from ..forms.speaker import AddForm
from . import LoginRequiredMixin


class AddView(LoginRequiredMixin, FormView):

    template_name = 'content/speakers_add.html'
    form_class = AddForm

    def form_valid(self, form, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return self.render_to_response(context)
