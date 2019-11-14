from quiz.models import Quiz
from quiz.models import Quiz_Detail
from quiz.models import Level

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

class QuizSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['url', 'name', 'level', 'category', 'is_active']
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
