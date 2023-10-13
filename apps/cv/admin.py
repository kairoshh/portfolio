from django.contrib import admin

from apps.cv.models import Cv, CategoryProject, Project, ProjectImage, ProjectStack


admin.site.register(Cv)
admin.site.register(CategoryProject)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 5

class ProjectStackInline(admin.TabularInline):
    model = ProjectStack
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        ProjectImageInline,
        ProjectStackInline
    )

admin.site.register(Project, ProjectAdmin)