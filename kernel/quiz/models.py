import uuid


from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _

from .queryset.managers import QuizManager_practice
from .queryset.managers import CandidateManager_practice

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
    # candidate_manager = CandidateManager()
    candidate_manager = CandidateManager_practice()

    class Meta:
        permissions = (
            ('can_take_quiz', 'Can Take Quiz'),
        )

    def get_total_correct_count(self):
        active_quizes_queryset = Quiz.quiz_manager.all().filter(is_active=True)
        if len(active_quizes_queryset) > 0:
            current_quiz = active_quizes_queryset[0]
            quiz_questions = current_quiz.questions.all()
            question_answers = Answers.answere_manager.filter(id__in=quiz_questions.values('possible_choices__id'))

            pass
        else:
            return 0 # this user is not participating in a quiz
        # return self.quiz_id.all()
        # return self.candidate_manager.filter(pk=id)
        pass
        

    def get_all_quiz_questions(self):
        active_quizes_queryset = Quiz.quiz_manager.all().filter(is_active=True)
        if len(active_quizes_queryset) > 0:
            current_quiz = active_quizes_queryset[0]
            quiz_questions = current_quiz.questions.all()
            question_answers = Answers.answere_manager.filter(id__in=quiz_questions.values('possible_choices__id'))

            pass
        else:
            return 0
        pass
        

    def __str__(self):
        return f"{self.user_id.user.first_name} {self.user_id.user.last_name}"






class UserQuerySet(models.QuerySet):
    def best_score(self):
        each_time_candidate = Candidate.objects.filter(user_id=id)
   

class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
        
    def get_best_score(self):
        return self.get_queryset().best_score()




class User(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    objects = models.Manager()
    user_manager = UserManager()


class CandidateQuestionAnswerQuerySet(models.QuerySet):
    pass

class CandidateQuestionAnswerManager(models.Manager):
    def get_queryset(self):
        return CandidateQuestionAnswerQuerySet(self.model, using=self._db)

    def get_answers_of_candidat(self, candidate):
        return self.get_queryset().filter(candidate_id__id=candidate.id)


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
    


class AnswerQuerySet(models.QuerySet):
    pass


class AnswerManager(models.Manager):
    def get_queryset(self):
        return AnswerQuerySet(self.model, using=self._db)
    

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

class QuestionQuerySet(models.QuerySet):
    pass

class QuestionManager(models.Manager):
    def get_queryset(self):
        return Question(self.model, using=self._db)
    
    # def get_quiz_questions(self):
    #     return self.get_queryset().filter(questions)



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

    # def get_quiz_questions(self, quiz):
    #     return self.question_manager.filter(id__in=quiz.get_question_ids())


class QuizQuerySet(models.QuerySet):
    def get_candidates(self):
        return Candidate.objects.all().filter(id__in=self.all().values('Candidate_fk__id')) # be ja candidate bayad yser bashe ...
    def get_all_users(self):
        # return Candidate.candidate_manager.get_users().filter(id__in=self.all().values('Candidate_fk__id'))  # quiz haE ka hazf shodan bug mide 
        return Candidate.candidate_manager.get_users().filter(id__in=self.get_candidates().values('user_id__id'))
        

class QuizManager(models.Manager):
    def get_queryset(self):
        return QuizQuerySet(self.model, using=self._db)
    
    def get_candidates(self): # all candidates who took a quiz (some candidates can correspond to a single user)
        return self.get_queryset().get_candidates() 
    
    def get_users(self): # all users who took a quiz
        return self.get_queryset().get_all_users()  

    def total_quiz_count(self): # total number of quizes
        return len(self.get_queryset())

    def get_questions(self, quiz): # TODO : remove
        return quiz.questions.all()

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

    

    # class Meta:
    #     permissions = (
    #         ('can_take_quiz', 'Can Take Quiz'),
    #     )

    def __str__(self):
        return f'{self.title}'

class QuizDetail(models.Model):
    id = models.UUIDField(primary_key=True , default = uuid.uuid4 , editable= False)
    score_per_question = models.IntegerField(default=1 )
    banner = models.ImageField('upload/quiz/',null=True,blank=True)
    teacher = models.ForeignKey('quiz.User', on_delete=models.SET_NULL,null=True)
    time_limit = models.BooleanField(_("Time Limit"), default = False)
    time_per_question = models.TimeField(_("Time Per Question"))

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
