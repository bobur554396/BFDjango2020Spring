import logging

from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from demo.core.models import Author, Book
from demo.core.serializers import AuthorSerializer, BookShortSerializer, BookFullSerializer

logger = logging.getLogger(__name__)


class AuthorListViewSet(viewsets.ModelViewSet):
    # queryset = Author.objects.annotate(books_count=Count('books'),
    #                                    book_min_price=Min('books__price'),
    #                                    book_max_price=Max('books__price'))
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def get_queryset(self):
        if self.action == 'list':
            return Author.objects.prefetch_related('books')
        return Author.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Author object created, ID: {serializer.instance}')
        logger.info(f'Author object created, ID: {serializer.instance}')
        logger.warning(f'Author object created, ID: {serializer.instance}')
        logger.error(f'Author object created, ID: {serializer.instance}')
        logger.critical(f'Author object created, ID: {serializer.instance}')

    @action(methods=['GET'], detail=False)
    def top_ten(self, request):
        # TODO Get top 10 author
        return Response('top ten authors')

    @action(methods=['PUT'], detail=True)
    def set_rating(self, request, pk):
        author = self.get_object()
        # Variant 2
        # author = get_object_or_404(Author, id=pk)

        # Variant 1
        # try:
        #     author = Author.objects.get(id=pk)
        # except Author.DoesNotExist:
        #     raise Http404
        author.set_new_rating(request.data.get('value'))
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class BookViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return Book.objects.select_related('author')
        return Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookShortSerializer
        if self.action == 'retrieve':
            return BookFullSerializer
        if self.action in ['test', 'test2', 'test3']:
            return 1
        return BookShortSerializer

    @action(methods=['GET'], detail=False)
    def price_report(self, request):
        data = [
            Book.objects.aggregate(Avg('price')),
            Book.objects.aggregate(max_price=Max('price')),
            Book.objects.aggregate(Min('price')),
            Book.objects.aggregate(Sum('price')),
            Author.objects.values('id').annotate(Count('books'))
        ]
        return Response(data)

    @action(methods=['POST'], detail=True)
    def test2(self, request, pk):
        serializer = self.get_serializer()

        return Response('data')

    @action(methods=['POST'], detail=True)
    def test3(self, request, pk):
        serializer = self.get_serializer()

        return Response('data')
