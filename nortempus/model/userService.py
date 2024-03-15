from django.db import models

class UserService(models.Model):
    # User attributes
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    total_score = models.IntegerField()
    volunteer_count = models.IntegerField()
    plan_choices = [
        ('Basis', 'Basis'),
        ('Premium', 'Premium')
    ]
    plan = models.CharField(max_length=10, choices=plan_choices)

    # Relationships
    user1 = models.ForeignKey('User', related_name='user1_services', on_delete=models.CASCADE)
    user2 = models.ForeignKey('User', related_name='user2_services', on_delete=models.CASCADE)
    service1 = models.ForeignKey('Service', related_name='service1_userservices', on_delete=models.CASCADE)
    service2 = models.ForeignKey('Service', related_name='service2_userservices', on_delete=models.CASCADE)

