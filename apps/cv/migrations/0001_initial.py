# Generated by Django 3.2.7 on 2023-09-30 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='post/images', verbose_name='картинка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoty_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=121, verbose_name='название')),
                ('description', models.TextField(verbose_name='описние')),
                ('image', models.ImageField(upload_to='post/images')),
                ('link', models.CharField(max_length=123)),
                ('link_code', models.CharField(max_length=123, null=True)),
                ('time_development', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='cv.categoryproject')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123, verbose_name='название')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_stacks', to='cv.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/images', verbose_name='картинка')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_imgies', to='cv.project')),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123, verbose_name='название')),
                ('email', models.EmailField(max_length=123)),
                ('phone_number', models.PositiveIntegerField(verbose_name='номер телефона')),
                ('work_experience', models.TextField(max_length=300, verbose_name='опыт работы')),
                ('stack', models.CharField(max_length=200, verbose_name='навык')),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Middle_junior', 'Middle_junior'), ('Strong_junior', 'Strong_junior'), ('Middle', 'Middle'), ('Strong_middle', 'Strong_middle'), ('Senior', 'Senior')], max_length=121)),
                ('direction', models.CharField(max_length=123)),
                ('avatar', models.ImageField(upload_to='avatar/images', verbose_name='аватарка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cvies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
