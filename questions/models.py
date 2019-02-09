from django.db import models

# Create your models here.


class VideoInterview(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=True)
    job_seekers = models.ManyToManyField(
        'JobSeeker', verbose_name='Соискатели', related_name='video_interview'
    )
    questions = models.ManyToManyField(
        'Question', verbose_name='Вопросы', related_name='video_interview'
    )

    class Meta:
        verbose_name = 'Видео-интервью'
        verbose_name_plural = 'Видео-интервью'

    def __str__(self):
        return self.title

    def get_job_seekers(self):
        return ',\n'.join([p.name for p in self.job_seekers.all()])

    def get_questions(self):
        return ',\n'.join([p.title for p in self.questions.all()])


class Question(models.Model):
    title = models.CharField(
        max_length=50, null=False, verbose_name='Название'
    )
    text = models.TextField(null=False, verbose_name='Содержание вопроса')
    seconds_to_answer = models.IntegerField(
        null=False, default=60, verbose_name='Время на ответ (в секундах)'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Имя')

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self):
        return self.name
