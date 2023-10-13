from apps.cv.serializers import  CvSerializer, ProjectSerializer, ProjectImageSerializer, ProjectStackSeriaizer, CategoryProjectSeializer

from rest_framework.viewsets import ModelViewSet
from apps.cv.models import Cv, CategoryProject, Project, ProjectImage, ProjectStack


from rest_framework.permissions import IsAuthenticated


class CvView(ModelViewSet):
    queryset = Cv.objects.all()
    serializer_class = CvSerializer
    permission_classes = (IsAuthenticated,)


class CategoryProjectView(ModelViewSet):
    queryset = CategoryProject.objects.all()
    serializer_class = CategoryProjectSeializer
    permission_classes = (IsAuthenticated, )


class ProjecView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)


class ProjectImageView(ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = (IsAuthenticated,)


class ProjectStackView(ModelViewSet):
    queryset = ProjectStack.objects.all()
    serializer_class = ProjectStackSeriaizer
    permission_classes = (IsAuthenticated, )


