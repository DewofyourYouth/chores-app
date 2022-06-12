from django.contrib import admin
from .models import Family, Parent, Child, Task


class FamilyAdmin(admin.ModelAdmin):
    model = Family
    list_display = ["id", "last_name"]


class ParentAdmin(admin.ModelAdmin):
    model = Parent
    list_display = [
        "first_name",
        "last_name",
    ]

    @admin.display
    def last_name(self, obj):
        return obj.family.last_name


class ChildAdmin(admin.ModelAdmin):
    model = Child
    list_display = [
        "first_name",
        "last_name",
        "birthday",
    ]

    @admin.display
    def last_name(self, obj):
        return obj.family.last_name


class TaskAdmin(admin.ModelAdmin):
    ordering = ["chore_type", "id"]
    model = Task
    list_display = [
        "id",
        "title",
        "points_value",
        "chore_type",
    ]


# Register your models here.
admin.site.register(Family, FamilyAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Task, TaskAdmin)
