# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework.serializers import ModelSerializer
from .models import Event


class EventSerializer(ModelSerializer):

    class Meta(object):
        model = Event
        exclude = []
