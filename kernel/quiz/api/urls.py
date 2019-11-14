from rest_framework import routers
from .views import QuizViewSets
from .views import LevelViewSets
from .views import CategoryViewSets
from .views import QuizDetailViewSets
from .views import  UserViewSets


router = routers.DefaultRouter()

router.register(r'quizes',QuizViewSets)
router.register(r'category',CategoryViewSets)
router.register(r'level',LevelViewSets)
router.register(r'quiz_detail',QuizDetailViewSets)
router.register(r'user',UserViewSets)