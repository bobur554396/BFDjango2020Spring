from django.urls import path

from demo.core.views import AuthorListAPIView

urlpatterns = [
    path('authors/', AuthorListAPIView.as_view())
]
