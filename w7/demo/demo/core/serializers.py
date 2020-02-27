from rest_framework import serializers

from demo.core.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)

    # email = serializers.EmailField()

    # def create(self, validated_data):
    #     created new instance
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     return instance

    class Meta:
        model = Author
        fields = ('id', 'name', 'email',)

    def validate_name(self, value):
        if ['/', '%'] in value:
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

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'is_published', 'author_id',)


class BookFullSerializer(BookShortSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta(BookShortSerializer.Meta):
        fields = BookShortSerializer.Meta.fields + ('author',)
