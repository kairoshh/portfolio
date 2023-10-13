from rest_framework import serializers

from django.contrib.auth import get_user_model
from apps.cv.models import Cv, CategoryProject, Project, ProjectImage, ProjectStack

User = get_user_model()

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields = (
            'id', 'user',
            'email', 'phone_number',
            'work_experience', 'stack',
            'level', 'direction',
            'avatar',
        )


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = (
            'id', 'project',
            'image', 
        )

class ProjectStackSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStack
        fields = (
            'id', 'project',
            'name',
        )
        

class ProjectSerializer(serializers.ModelSerializer):
    project_imagies = ProjectImageSerializer(many=True, read_only=True)
    project_stacks = ProjectStackSeriaizer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = (
            'id', 'name',
            'category', 'description',
            'image', 'link',
            'link_code', 'time_development',
            'project_imagies', 'project_stacks',
        )

class CategoryProjectSeializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = CategoryProject
        fields = (
            'id', 'name',
            'user', 'description',
            'image', 'projects',
        )

class UserSerializer(serializers.ModelSerializer):
    category_projects = CategoryProjectSeializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'id','username',
            'email','password',
            'first_name','last_name',
            'category_projects',
        )