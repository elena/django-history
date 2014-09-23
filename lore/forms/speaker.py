from django import forms
from ..models import Speaker


class SpeakerForm(forms.ModelForm):

    class Meta(object):
        model = Speaker
