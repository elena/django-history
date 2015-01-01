# -*- coding: utf-8 -*-
from django import forms
from lore.models import Speaker


class SpeakerFormMixin(forms.ModelForm):

    class Meta(object):
        model = Speaker


class AddForm(SpeakerFormMixin):

    pass