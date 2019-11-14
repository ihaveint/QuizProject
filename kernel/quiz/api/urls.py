from rest_framework import routers
from .views import QuizViewSets
from .views import LevelViewSets
from .views import CategoryViewSets


router = routers.DefaultRouter()

router.register(r'quizes',QuizViewSets)
router.register(r'category',CategoryViewSets)
router.register(r'level',LevelViewSets)