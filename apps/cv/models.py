from django.db import models

from django.contrib.auth import get_user_model
from apps.cv.choice import LEVEL

User = get_user_model()


class Cv(models.Model):
    name = models.CharField(max_length=123, verbose_name='Название')
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE,
        related_name='cvies', verbose_name='Пользователь'
    )
    email = models.EmailField(max_length=123,verbose_name='Электроная почта')
    phone_number = models.PositiveIntegerField(verbose_name='Номер телефона')
    work_experience = models.TextField(max_length=300, verbose_name='Опыт работы')
    stack = models.CharField(max_length=200, verbose_name='Навык')
    level = models.CharField(max_length=121, verbose_name='Уровень', choices=LEVEL, default='Junior')
    direction = models.CharField(max_length=123, verbose_name='Направлене')
    avatar = models.ImageField(upload_to='avatar/images', verbose_name='Аватарка')


    def __str__(self):
        return f'{self.name} {self.email} {self.phone_number}\
              {self.work_experience} {self.stack} {self.level} {self.direction} '


    

class CategoryProject(models.Model):
    name = models.CharField(max_length=123, verbose_name='Название')
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='categoty_projects', verbose_name='Пользователь'
    )
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='post/images', verbose_name='Картинка')

    def __str__(self):
        return f'{self.name} {self.description} '



class Project(models.Model):
    name = models.CharField(max_length=121, verbose_name='Название')
    category = models.ForeignKey(
        to=CategoryProject, on_delete=models.CASCADE,
        related_name='projects', verbose_name='Категория'
    )
    description = models.TextField(verbose_name='Описние')
    image = models.ImageField(upload_to='post/images', verbose_name='Картинка')
    link = models.URLField(max_length=123,verbose_name='Ссылка' )
    link_code = models.URLField(null=True, verbose_name='Ссылка на код')
    time_development = models.CharField(max_length=130, verbose_name='время разработки')

    def __str__(self):
        return f'{self.name} {self.category} {self.description} {self.link} {self.link_code} {self.time_development}'




class ProjectImage(models.Model):
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE,
        related_name='project_imagies', verbose_name='Проект'
    )
    image = models.ImageField(upload_to='post/images', verbose_name='Картинка')

    def __str__(self):
        return f'{self.project} '



class ProjectStack(models.Model):
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE,
        related_name='project_stacks', verbose_name='Проект'
    )
    name = models.CharField(max_length=123, verbose_name='Название')

    
    def __str__(self):
        return f'{self.project} {self.name} '


