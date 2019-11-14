from django.contrib import admin
# from .models import Question
# from .models import Quiz
# from .models import Student

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Quiz)
# admin.site.register(Student)


from .models import *
@admin.register(Candidate)
class Candidate_Admin(admin.ModelAdmin):
    fields = (
        ('quiz_id'),
        ('user_id'),
        ('no_correct','no_incorrent','no_unanswered','score'),
        ('time_start','time_end'),
        ('exam_date'),
    )

admin.site.register(User)

@admin.register(Candidate_Question_Answer)
class Candidate_Question_Answer_Admin(admin.ModelAdmin):
    fields = (
        ('candidate_id'),
        ('quiz_question_id'),
        ('candidate_answer','is_correct'),
        ('time_start','time_end'),
    )

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    fields = (
        ('option1','option2','option3','option4'),
        ('answer'),
    )
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Quiz_Detail)
admin.site.register(Question_Feedback)
admin.site.register(Level)
admin.site.register(Category)
