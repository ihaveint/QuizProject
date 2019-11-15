from django.db import models
from .queryset import QuizQuerySet_practice
from .queryset import CandidateQuerySet_practice
from .queryset import UserQuerySet
from .queryset import CandidateQuestionAnswerQuerySet
from .queryset import AnswerQuerySet
from .queryset import QuestionQuerySet

class QuizManager_practice(models.Manager):
    def get_queryset(self):
        return QuizQuerySet_practice(self.model, using=self._db)

    def test(self, value):
        return self.get_queryset().test(value)

    def candidates(self, quiz_id):
        return self.get_queryset().candidates(quiz_id)

    def all_candidates_history(self):
        return self.get_queryset().all_candidates_history()

    def total_quiz_count_scaler(self):
        return self.get_queryset().total_quiz_count_scaler()


class CandidateManager_practice(models.Manager):
    def get_queryset(self):
        return CandidateQuerySet_practice(self.model, using=self._db)
    
    def users(self):
        return self.get_queryset().users()
    
    def get_candidate_active_quiz(self, candidate_id):
        return self.get_queryset().get_candidate_active_quiz(candidate_id)

    def get_questions_of_active_quiz(self,candidate_id):
        return self.get_queryset().get_questions_of_active_quiz(candidate_id)

    def get_candidate_answers_for_activate_quiz(self,candidate_id):
        return self.get_queryset().get_candidate_answers_for_activate_quiz(candidate_id)

    def get_active_quiz_answers(self, candidate_id):
        return self.get_queryset().get_active_quiz_answers(candidate_id)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
    
    def get_best_score(self, user_id):
        return self.get_queryset().get_best_score(user_id)


class CandidateQuestionAnswerManager(models.Manager):
    def get_qureyset(self):
        return CandidateQuestionAnswerQuerySet(self.mode, using=self._db)
    

class AnswerManager(models.Manager):
    def get_queryset(self):
        return AnswerQuerySet(self.model, using=self._db)


class QuestionManager(models.Manager):
    def get_queryset(self):
        return QuestionQuerySet(self.model, using=self._db)