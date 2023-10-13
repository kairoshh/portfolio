from apps.cv.views import CvView, CategoryProjectView, ProjecView, ProjectStackView, ProjectImageView
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)


router = DefaultRouter()
router.register('cv', CvView),
router.register('category_project', CategoryProjectView),
router.register('project', ProjecView),
router.register('project_image', ProjectImageView),
router.register('project_stack', ProjectStackView)
urlpatterns = [
    path('token',  TokenObtainPairView.as_view()),
   
]

urlpatterns += router.urls
