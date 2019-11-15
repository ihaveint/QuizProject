from django.db.models import QuerySet
from django.db.models import prefetch_related_objects



class QuizQuerySet_practice(QuerySet):
    
    
    # def get_candidates(self, quiz_id):
    #     quiz = self.get(pk=quiz_id)
    #     queryset = quiz.Candidate_fk.all()
    #     return queryset

    def all_candidates_history(self):
        queryset = self.none()
        for quiz in self.all():
            queryset = queryset.union(quiz.Candidate_fk.all())
        return queryset

    def get_all_candidates_history(self, id):
        return self.all_candidates_history().filter(quiz_id=id)

    def total_quiz_count_scaler(self):
        return len(self.all())



    def get_quiz_questions(self, quiz_id):
        return self.get(pk=quiz_id).questions.all()


class CandidateQuerySet_practice(QuerySet):
    def users(self):
        return self.all().users()

    def get_candidate_active_quiz(self, candidate_id):
        candidate = self.all().get(pk=candidate_id)
        return candidate.quiz_id.get(is_active=True)

    def get_candidate_quizes(self, candidate_id):
        candidate = self.all().get(pk=candidate_id)
        return candidate.quiz_id.all()
    

    def get_questions_of_active_quiz(self, candidate_id):
        active_quiz = self.get_candidate_active_quiz(candidate_id)
        return active_quiz.questions.all()
    
    def get_active_quiz_answers(self,candidate_id):
        queryset = self.none()
        questions = self.get_questions_of_active_quiz(candidate_id)
        for question in questions:
            queryset = queryset.union(question.possible_choices.all())
        return queryset

    def get_candidate_answers_for_activate_quiz(self, candidate_id):
        candidate = self.get(pk=candidate_id)
        related_questions = self.get_questions_of_active_quiz(candidate_id)
        related_candidate_answers = candidate.question_answers.filter(quiz_question_id__id__in=related_questions.values('id'))
        return related_candidate_answers
        
    
    def get_all_correct_answered_questions(self, candidate_id): # wip
        related_candidate_answers = self.get_active_candidate_answers(candidate_id)
        related_quiz_answers = self.get_active_quiz_answers(candidate_id)
        
        for candidate_answer in related_candidate_answers:
            related_question = candidate_answer.quiz_question_id
            related_question_answer = related_question.possible_choices


        return related_candidate_answers.filter()

    
class UserQuerySet(QuerySet):
    def get_best_score(self, user_id):
        relater_user = self.get(pk=user_id)
        related_candidates = relater_user.Candidate_fk.all()
        response = 0
        for candidate in related_candidates:
            response = max(response,candidate.score)
        return response

class CandidateQuestionAnswerQuerySet(QuerySet):
    pass


class AnswerQuerySet(QuerySet):
    pass

class QuestionQuerySet(QuerySet):
    pass