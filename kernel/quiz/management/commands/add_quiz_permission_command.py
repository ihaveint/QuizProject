from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from quiz.models import Quiz
class Command(BaseCommand):
    help = "Add can_take_quiz permission"

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Quiz)
        if len(Permission.objects.all().filter(codename="can_take_quiz")) == 0:
            permission = Permission.objects.create(
                codename='can_take_quiz',
                name='Can Take Quiz',
                content_type=content_type,
            )
