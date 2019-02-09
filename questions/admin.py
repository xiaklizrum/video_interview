from django.contrib import admin

# Register your models here.
from questions.models import VideoInterview, Question, JobSeeker


class VideoInterviewAdmin(admin.ModelAdmin):
    model = VideoInterview
    list_display = ['title', 'get_job_seekers', 'get_questions']


admin.site.register(VideoInterview, VideoInterviewAdmin)


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['title', 'text', 'seconds_to_answer']


admin.site.register(Question, QuestionAdmin)


class JobSeekerAdmin(admin.ModelAdmin):
    model = JobSeeker
    list_display = ['name']


admin.site.register(JobSeeker, JobSeekerAdmin)
