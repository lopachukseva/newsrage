from rest_framework import serializers

from news.models import Category, News


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = News
        fields = ("title", "photo", "content", "slug", "category", "time_create", "time_update")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug")
