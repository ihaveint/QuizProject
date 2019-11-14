from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType




class Candidate(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    quiz_id = models.ManyToManyField('quiz.Quiz',null=True)
    user_id = models.ForeignKey('quiz.User',on_delete=models.CASCADE, related_name='Candidate_fk')
    no_correct = models.IntegerField(default=0)
    no_incorrent = models.IntegerField(default=0)
    no_unanswered = models.IntegerField(default = 0)
    score = models.IntegerField(default = 0)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    exam_date = models.DateTimeField()


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Candidate_Question_Answer(models.Model):
    answer_choices = (('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'),)
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    candidate_id = models.ForeignKey('quiz.Candidate',on_delete = models.CASCADE)
    quiz_question_id = models.ForeignKey('quiz.Question' , on_delete= models.CASCADE , related_name='candidate_answer')
    candidate_answer = models.CharField(max_length = 1 , choices = answer_choices)
    is_correct = models.BooleanField(default=False , null=True , blank=True )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

class Answers(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    answer_choices = (('a', option1),('b',option2),('c',option3),('d',option4),)
    answer = models.CharField(max_length=20,choices=answer_choices)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Answers"

class Question(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    text = models.CharField(max_length=300)
    image = models.ImageField('upload/question/' , null=True , blank=True)
    possible_choices = models.ForeignKey('quiz.Answers', on_delete=models.SET_NULL,null=True)
    quiz_id = models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Quiz(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    quiz_detail = models.OneToOneField('quiz.Quiz_Detail',on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey('quiz.Category',on_delete=models.SET_NULL,null=True)
    level = models.ForeignKey('quiz.Level',on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('can_take_quiz', 'Can Take Quiz'),
        )

class Quiz_Detail(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    score_per_question = models.IntegerField(default=1 )
    banner = models.ImageField('upload/quiz/',null=True,blank=True)
    teacher = models.ForeignKey('quiz.User', on_delete=models.SET_NULL,null=True)
    time_limit = models.BooleanField(default=True)
    time_per_question = models.TimeField()

class Question_Feedback(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    user_id = models.ForeignKey('quiz.User', on_delete=models.SET_NULL,null=True)
    question_id = models.ForeignKey('quiz.Question', on_delete=models.CASCADE)

class Level(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)


class Category(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"
