from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Resumedata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(('電話番号'), max_length=15, null=True, default=None)
    twitter = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=20, blank=True)
    school1 = models.CharField(max_length=40, null=True)
    major1 = models.CharField(max_length=40, null=True)
    s_start1 = models.CharField(max_length=8, null=True)
    s_end1 = models.CharField(max_length=8, null=True)
    school2 = models.CharField(max_length=40, null=True)
    major2 = models.CharField(max_length=40, null=True)
    s_start2 = models.CharField(max_length=8, null=True)
    s_end2 = models.CharField(max_length=8, null=True)
    school3 = models.CharField(max_length=40, blank=True)
    major3 = models.CharField(max_length=40, blank=True)
    s_start3 = models.CharField(max_length=8, blank=True)
    s_end3 = models.CharField(max_length=8, blank=True)
    aboutme1 = models.CharField(max_length=300, null=True)
    aboutme2 = models.CharField(max_length=300, null=True)
    exp1 = models.CharField(max_length=40, null=True)
    position1 = models.CharField(max_length=40, null=True)
    e_start1 = models.CharField(max_length=8, null=True)
    e_end1 = models.CharField(max_length=8, null=True)
    exp2 = models.CharField(max_length=40, null=True)
    position2 = models.CharField(max_length=40, null=True)
    e_start2 = models.CharField(max_length=8, null=True)
    e_end2 = models.CharField(max_length=8, null=True)
    exp3 = models.CharField(max_length=40, null=True)
    position3 = models.CharField(max_length=40, null=True)
    e_start3 = models.CharField(max_length=8, null=True)
    e_end3 = models.CharField(max_length=8, null=True)
    skill_type1 = models.CharField(max_length=20, null=True)
    skill_level1 = models.CharField(max_length=20, null=True)
    skill_type2 = models.CharField(max_length=20, null=True)
    skill_level2 = models.CharField(max_length=20, null=True)
    skill_type3 = models.CharField(max_length=20, null=True)
    skill_level3 = models.CharField(max_length=20, null=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.user.username

def create_resumedata(sender, **kwargs):
    if kwargs['created']:
        resume_data = Resumedata.objects.create(user=kwargs['instance'])

post_save.connect(create_resumedata, sender=User)


def save_resumedata(sender, **kwargs):
    if kwargs['created']:
        resume_data = Resumedata.objects.create(user=kwargs['instance'])

post_save.connect(create_resumedata, sender=User)