import uuid


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _

from .queryset.managers import QuizManager_practice
from .queryset.managers import CandidateManager_practice
from .queryset.managers import UserManager
from .queryset.managers import CandidateQuestionAnswerManager
from .queryset.managers import AnswerManager
from .queryset.managers import QuestionManager

class Candidate(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    quiz_id = models.ManyToManyField('quiz.Quiz',null=True, related_name='Candidate_fk')
    user_id = models.ForeignKey('quiz.User',on_delete=models.CASCADE, related_name='Candidate_fk')
    no_correct = models.IntegerField(default=0)
    no_incorrent = models.IntegerField(default=0)
    no_unanswered = models.IntegerField(default = 0)
    score = models.IntegerField(default = 0)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    exam_date = models.DateTimeField()

    objects = models.Manager()
    candidate_manager = CandidateManager_practice()

    class Meta:
        permissions = (
            ('can_take_quiz', 'Can Take Quiz'),
        )

    def __str__(self):
        return f"{self.user_id.user.first_name} {self.user_id.user.last_name}"




class User(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    objects = models.Manager()
    user_manager = UserManager()

    def __str__(self):
        return f"{self.user.first_name} , {self.user.last_name}"


class Candidate_Question_Answer(models.Model):
    answer_choices = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'),('skip','SKIP'))
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    candidate_id = models.ForeignKey('quiz.Candidate',on_delete = models.CASCADE , related_name='question_answers')
    quiz_question_id = models.ForeignKey('quiz.Question' , on_delete= models.CASCADE , related_name='question_answers')
    candidate_answer = models.CharField(max_length = 20 , choices = answer_choices)
    is_correct = models.BooleanField(default=False , null=True , blank=True )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    objects = models.Manager()
    candidate_question_answer_manager = CandidateQuestionAnswerManager()


    def save(self, *args, **kwargs):
        super(Candidate_Question_Answer, self).save(*args, **kwargs)    

    def __str__(self):
        return f"candidate answer : {self.candidate_id , self.quiz_question_id}"    



class Answers(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    answer_choices = (('a', 'A'),('b','B'),('c','C'),('d','D'),)
    answer = models.CharField(max_length=20,choices=answer_choices)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    objects = models.Manager()
    answere_manager = AnswerManager()

    class Meta:
        verbose_name_plural = "Answers"

    def save(self, *args, **kwargs):
        super(Answers, self).save(*args, **kwargs)    

    def __str__(self):
        return f"answer options : {self.option1}, {self.option2}, {self.option3}, {self.option4}"

class Question(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    text = models.CharField(max_length=300)
    image = models.ImageField('upload/question/' , null=True , blank=True)
    possible_choices = models.ForeignKey('quiz.Answers', on_delete=models.SET_NULL,null=True)
    quiz_id = models.ForeignKey('quiz.Quiz',on_delete=models.CASCADE, related_name='questions')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    question_manager = QuestionManager()

    def __str__(self):
        return f"question text : {self.text}"


class Quiz(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    quiz_detail = models.OneToOneField('quiz.QuizDetail',on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey('quiz.Category',on_delete=models.SET_NULL,null=True)
    level = models.ForeignKey('quiz.Level',on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    objects = models.Manager()
    quiz_manager = QuizManager_practice()

    def __str__(self):
        return f'{self.title}'

class QuizDetail(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    score_per_question = models.IntegerField(default=1 )
    banner = models.ImageField('upload/quiz/',null=True,blank=True)
    teacher = models.ForeignKey('quiz.User', on_delete=models.SET_NULL,null=True)
    time_limit = models.BooleanField(_("Time Limit"), default = False)
    time_per_question = models.TimeField(_("Time Per Question"))

    def __str__(self):
        return f"quiz by : {self.teacher.user.first_name} , {self.teacher.user.last_name}"

class Question_Feedback(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    user_id = models.ForeignKey('quiz.User', on_delete=models.SET_NULL,null=True)
    question_id = models.ForeignKey('quiz.Question', on_delete=models.CASCADE)

    def __str__(self):
        return f"feedback title : {self.title}"

class Level(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return f"{self.slug}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.slug}"
