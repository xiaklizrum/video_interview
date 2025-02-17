# Generated by Django 2.1.5 on 2019-02-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Соискатель',
                'verbose_name_plural': 'Соискатели',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Содержание вопроса')),
                ('seconds_to_answer', models.IntegerField(default=60, verbose_name='Время на ответ (в секундах)')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='VideoInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('job_seekers', models.ManyToManyField(related_name='video_interview', to='questions.JobSeeker', verbose_name='Соискатели')),
                ('questions', models.ManyToManyField(related_name='video_interview', to='questions.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Видео-интервью',
                'verbose_name_plural': 'Видео-интервью',
            },
        ),
    ]
