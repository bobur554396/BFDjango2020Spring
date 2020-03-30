from django.urls import path

from demo.core.views import AuthorListAPIView, AuthorDetailAPIView
#
# urlpatterns = [
#     path('authors/', AuthorListAPIView.as_view()),
#     # path('authors/top-ten/', AuthorListAPIView.as_view()),
#     # path('authors/<int:author_id>/', AuthorDetailAPIView.as_view())
# ]
from demo.core.views_viewsets import AuthorListViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('authors', AuthorListViewSet)
router.register('books', BookViewSet)

urlpatterns = router.urls
