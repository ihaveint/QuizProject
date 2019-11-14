from rest_framework import viewsets
from .serializers import QuizSerializer
from quiz.models import Quiz
from quiz.models import Category
from quiz.models import Level


class QuizViewSets(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class LevelViewSets(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = QuizSerializer

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = QuizSerializer
