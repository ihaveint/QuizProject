from rest_framework import viewsets
from .serializers import QuizSerializer
from .serializers import CategorySerializer
from .serializers import LevelSerializer
from .serializers import QuizDetailSerializer
from .serializers import UserSerializer
from .serializers import QuestionFeedbackSerializer
from .serializers import QuestionSerializer
from .serializers import Answerserializer
from .serializers import CandidateQuestionAnswerSerializer
from .serializers import CandidateSerializer
from quiz.models import Quiz
from quiz.models import Category
from quiz.models import Level
from quiz.models import QuizDetail
from quiz.models import User
from quiz.models import Question_Feedback
from quiz.models import Question
from quiz.models import Answers
from quiz.models import Candidate_Question_Answer
from quiz.models import Candidate

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


class QuestionFeedbackViewSets(viewsets.ModelViewSet):
    queryset = Question_Feedback.objects.all()
    serializer_class = QuestionFeedbackSerializer

class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswersViewSets(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = Answerserializer

class CandidateQuestionAnswerViewSets(viewsets.ModelViewSet):
    queryset = Candidate_Question_Answer.objects.all()
    serializer_class = CandidateQuestionAnswerSerializer

class CandidateViewSets(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer