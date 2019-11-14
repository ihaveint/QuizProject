from rest_framework import viewsets
from .serializers import QuizSerializer
from .serializers import CategorySerializer
from .serializers import LevelSerializer
from .serializers import QuizDetailSerializer
from .serializers import UserSerializer
from quiz.models import Quiz
from quiz.models import Category
from quiz.models import Level
from quiz.models import QuizDetail
from quiz.models import User


class QuizViewSets(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class LevelViewSets(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizDetailViewSets(viewsets.ModelViewSet):
    queryset = QuizDetail.objects.all()
    serializer_class = QuizDetailSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer