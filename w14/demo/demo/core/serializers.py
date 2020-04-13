from rest_framework import serializers

from demo.core.models import Author, Book


class BookShortSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'is_published', 'author_id', 'author_name',)


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(default=0)
    book_min_price = serializers.IntegerField(default=0)
    book_max_price = serializers.IntegerField(default=0)
    books = BookShortSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'photo', 'email', 'books_count', 'book_min_price',
                  'book_max_price', 'books',)

    def validate_name(self, value):
        if '/' in value:
            raise serializers.ValidationError('invalid char in name field')
        return value

    def validate(self, attrs):
        # check object level validation,
        # if any raise serializer.ValidationError
        return attrs


class AuthorSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    email = serializers.CharField(max_length=300)

    # def to_internal_value(self, data):
    #     pass
    #
    # def to_representation(self, instance):
    #     pass
    #
    # def create(self, validated_data):
    #     pass
    #
    # def update(self, instance, validated_data):
    #     pass


class BookShortSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'is_published', 'author_id', 'author_name',)


class BookFullSerializer(BookShortSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta(BookShortSerializer.Meta):
        fields = BookShortSerializer.Meta.fields + ('author',)
