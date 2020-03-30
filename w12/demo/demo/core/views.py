from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from demo.core.models import Author
from demo.core.serializers import AuthorSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import HttpRequest, HttpResponse, JsonResponse, Http404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework import mixins


class AuthorListAPIView(mixins.ListModelMixin,
                        generics.GenericAPIView):
    # http_method_names = ['GET', 'PUT']

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # lookup_field = 'author_id'
    # permission_classes = ()
    permission_classes = (IsAuthenticated,)

    # authentication_classes = (JSONWebTokenAuthentication,)
    def top_ten(self, request):
        pass

    def get(self, request, *args, **kwargs):
        # self.top_ten()
        return self.list(request, *args, **kwargs)


class AuthorDetailAPIView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'author_id'

    # filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    # filter_kwargs = {'pk': self.kwargs['pk']}
    # filter_kwargs = {'pk': 2}
    # obj = get_object_or_404(queryset, pk=2)

    # (2, 3, 4)
    # {'a': 1, 'b': 2}
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AuthorCreateUpdateAPIView(mixins.CreateModelMixin,
                                generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     serializer = AuthorSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
