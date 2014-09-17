from django import forms
from ..models import Talk


class TalkForm(forms.ModelForm):

    class Meta(object):
        model = Talk
