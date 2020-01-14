# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class AuthenticationGoogle(TemplateView):
    template_name = "authen/index.html"
