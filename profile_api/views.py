from django.shortcuts import render
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore

class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView festures"""
        an_apiview = [
            'Uses HTTp method as fucntions (get, post, path, put, delete)',
            'Is similar to a traditional Django views',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})