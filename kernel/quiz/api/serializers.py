from quiz.models import Quiz
from quiz.models import Category
from quiz.models import Level
from quiz.models import QuizDetail
from quiz.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

class QuizSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['url', 'title', 'level', 'category' , 'quiz_detail' , 'is_active']
        lookup_field = 'pk',
        depth = 2

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

class QuizDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = QuizDetail
        fields = ['url' , 'teacher', 'score_per_question' , 'time_limit', 'time_per_question']
        lookup_field = 'id',


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = []
        lookup_field = 'pk',