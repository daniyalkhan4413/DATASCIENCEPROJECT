from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    headline = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True,default='avatar.svg')
    skills = models.ManyToManyField('Skill', null=True)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True
    )


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class JobPosting(models.Model):

    title = models.TextField(max_length=200,null=True)

    created = models.DateTimeField(auto_now_add=True)

    company = models.CharField(max_length=100,null= True)

    jobtype = models.CharField(max_length=100,null=True)

    salary = models.IntegerField(null=True)

    location = models.CharField(max_length=200,null=True)

    required_skills = models.ManyToManyField(Skill, blank=True)

    description = models.TextField(max_length=500,null=True)

    appliedusers = models.ManyToManyField(User)




class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)