from rest_framework import serializers

from questions.models import VideoInterview, JobSeeker, Question


class VideoInterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoInterview
        fields = ('title', 'job_seekers', 'questions')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'text', 'seconds_to_answer')


class JobSeekerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobSeeker
        fields = ('name', 'video_interview')
