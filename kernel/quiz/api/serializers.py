from quiz.models import Quiz
from quiz.models import Category
from quiz.models import Level

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

class QuizSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['url', 'title', 'level', 'category', 'is_active']
        lookup_field = 'pk',
        depth = 1

class LevelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['url', 'slug']
        lookup_field = 'slug',

class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'slug']
        lookup_field = 'slug',
