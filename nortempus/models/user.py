from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    password = models.CharField(max_length=50)
    total_score = models.IntegerField()
    volunteer_count = models.IntegerField()
    plan_choices = [
        ('Basis', 'Basis'),
        ('Premium', 'Premium')
    ]
    plan = models.CharField(max_length=10, choices=plan_choices)

    def __str__(self):
        return self.name
