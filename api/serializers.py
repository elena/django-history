# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework.serializers import ModelSerializer
from events.models import Event
from lore.models import Category, Talk, Speaker


class EventSerializer(ModelSerializer):

    class Meta(object):
        model = Event
        exclude = []


class CategorySerializer(ModelSerializer):

    class Meta(object):
        model = Category
        exclude = []


class TalkSerializer(ModelSerializer):

    class Meta(object):
        model = Talk
        exclude = []


class SpeakerSerializer(ModelSerializer):

    class Meta(object):
        model = Speaker
        exclude = []
