from django.db import models

'''
---------------------------------------------
Model       : Country
Description : n/a
---------------------------------------------
'''
class Country(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Country",
                            blank=False,
                            null=False)

    def __str__(self):
        return self.name


'''
---------------------------------------------
Model       : School
Description : n/a
---------------------------------------------
'''
class School(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="School Name",
                            blank=False,
                            null=False)
    address = models.TextField(max_length=250,
                               verbose_name="School Address",
                               blank=True,
                               null=True)
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.name


'''
---------------------------------------------
Model       : Group
Description : n/a
---------------------------------------------
'''
class Group(models.Model):
    id = models.CharField(max_length=5,
                          verbose_name="Group ID",
                          primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name="Group Name",
                            blank=False,
                            null=False)
    description = models.TextField(max_length=250,
                                   verbose_name="Group Description",
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name


'''
---------------------------------------------
Model       : Section
Description : n/a
---------------------------------------------
'''
class Section(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Section Name",
                            blank=False,
                            null=False)
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              verbose_name="Group")
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               verbose_name="School")

    def __str__(self):
        return self.name

'''
---------------------------------------------
Model       : UserType
Description : n/a
---------------------------------------------
'''
class UserType(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Type Name",
                            blank=False,
                            null=False)
    description = models.TextField(max_length=250,
                                   verbose_name="Type Description",
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name

'''
---------------------------------------------
Model       : User
Description : n/a
---------------------------------------------
'''
class User(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Full Name",
                            blank=False,
                            null=False)
    phone = models.CharField(max_length=20,
                             verbose_name="Phone Number",
                             blank=True,
                             null=True)
    user_type = models.ForeignKey(UserType,
                              on_delete=models.CASCADE,
                              verbose_name="User Type")

    def __str__(self):
        return self.name


'''
---------------------------------------------
Model       : Subject
Description : n/a
---------------------------------------------
'''
class Subject(models.Model):
    title = models.CharField(max_length=100,
                            verbose_name="Subject Title",
                            blank=False,
                            null=False)
    description = models.TextField(max_length=250,
                             verbose_name="Subject Description",
                             blank=True,
                             null=True)
    users = models.ManyToManyField(User,
                                   through="UserSubject",
                                   through_fields=('subject', 'user'))

    def __str__(self):
        return self.title

'''
---------------------------------------------
Model       : UserSubject
Description : n/a
---------------------------------------------
'''
class UserSubject(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE)


'''
---------------------------------------------
Model       : Time
Description : n/a
---------------------------------------------
'''
class Time(models.Model):
    hour = models.TimeField(verbose_name="Start Time",
                            null=False,
                            blank=False)

'''
---------------------------------------------
Model       : Schedule
Description : n/a
---------------------------------------------
'''
class Schedule(models.Model):
    DAYS = [('Sun', 'Sunday'),
            ('Mon', 'Monday'),
            ('Tue', 'Tuesday'),
            ('Wed', 'Wednesday'),
            ('Thu', 'Thursday'),
            ('Fri', 'Friday'),
            ('Sat', 'Saturday')]
    day = models.CharField(max_length=30,
                            verbose_name="Class Time(Day of Week)",
                            choices=DAYS,
                            blank=False,
                            null=False)
    hour = models.ForeignKey(Time,
                             on_delete=models.CASCADE)

'''
---------------------------------------------
Model       : UserSubjectSchedule
Description : n/a
---------------------------------------------
'''
class UserSubjectSchedule(models.Model):
    schedule = models.ForeignKey(Schedule,
                                 on_delete=models.CASCADE)
    user_subject = models.ForeignKey(UserSubject,
                                     on_delete=models.CASCADE)