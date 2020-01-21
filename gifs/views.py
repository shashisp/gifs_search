# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests

from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.response import Response


class HomePageView(TemplateView):
    template_name = "home.html"




class GifsViewSet(APIView):

    def get(self, request, format=None):
        query = request.GET.get("query", None)
        if not query:
        	raise exceptions.ValidationError("invalid parameter")
        url = "http://api.giphy.com/v1/gifs/search?q="+query+"&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO"
        url = url+"&limit=1"
        data = requests.get(url)
        return Response(data.json())
