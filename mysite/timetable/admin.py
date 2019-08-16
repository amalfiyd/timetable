from django.contrib import admin
from .models import School, Section, Group, \
    User, UserType, Subject, \
    UserSubject, Time, Schedule, \
    UserSubjectSchedule

# Register your models here.
admin.site.register(School)
admin.site.register(Section)
admin.site.register(Group)
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(Subject)
admin.site.register(UserSubject)
admin.site.register(Time)
admin.site.register(Schedule)
admin.site.register(UserSubjectSchedule)