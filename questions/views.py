from rest_framework import viewsets
from questions.models import JobSeeker, VideoInterview, Question
from questions.serializers import JobSeekerSerializer, VideoInterviewSerializer, QuestionSerializer


class VideoInterviewViewSet(viewsets.ModelViewSet):
    """
    API видео интервью
    """
    queryset = VideoInterview.objects.all()
    serializer_class = VideoInterviewSerializer


class JobSeekerViewSet(viewsets.ModelViewSet):
    """
    API соискателей работы
    """
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API вопросов
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
