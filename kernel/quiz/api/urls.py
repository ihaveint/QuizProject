from rest_framework import routers
from .views import QuizViewSets
from .views import LevelViewSets
from .views import CategoryViewSets
from .views import QuizDetailViewSets
from .views import  UserViewSets
from .views import QuestionFeedbackViewSets
from .views import QuestionViewSets
from .views import AnswersViewSets
from .views import CandidateQuestionAnswerViewSets
from .views import CandidateViewSets
from .views import AllCandidatesHistoryViewSet

router = routers.DefaultRouter()

router.register(r'quizes',QuizViewSets)
router.register(r'category',CategoryViewSets)
router.register(r'level',LevelViewSets)
router.register(r'quiz_detail',QuizDetailViewSets)
router.register(r'user',UserViewSets)
router.register(r'question_feedback',QuestionFeedbackViewSets)
router.register(r'question',QuestionViewSets)
router.register(r'answer',AnswersViewSets)
router.register(r'candidate_answer',CandidateQuestionAnswerViewSets)
router.register(r'candidate',CandidateViewSets)
router.register(r'candidates_history',AllCandidatesHistoryViewSet, base_name='candidate_history')