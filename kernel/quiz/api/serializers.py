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
        fields = ['url']
        lookup_field = 'pk',


class QuestionFeedbackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question_Feedback
        fields = ['url', 'title', 'message', 'user', 'question']
        lookup_field = 'pk',

class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'text', 'possible_choices', 'quiz', 'created', 'modified']
        lookup_field = 'pk',


class Answerserializer(HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ['url', 'option1', 'option2', 'option3', 'option4', 'answer', 'created', 'modified']
        lookup_field = 'pk',


class CandidateQuestionAnswerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Candidate_Question_Answer
        fields = ['url', 'candidate', 'quiz_question', 'candidate_answer', 'is_correct', 'time_start', 'time_end']
        lookup_field = 'pk',

class CandidateSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ['url', 'quiz', 'user', 'no_correct', 'no_incorrent', 'no_unanswered', 'score', 'time_start', 'time_end', 'exam_date']