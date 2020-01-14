# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class UserProfile(TemplateView):
    template_name = "user_profile/index.html"

    def get_context_data(self, **kwargs):
        user = User.objects.get_by_natural_key(self.request.user)
        return {'user': user}
