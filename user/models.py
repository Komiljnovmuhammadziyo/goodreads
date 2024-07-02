from django.contrib.auth.models import AbstractUser
from django.db import models

class Follow(models.Model):
    user_from = models.ForeignKey('CustomUser', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('CustomUser', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to')

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')), default='male')
    followers = models.ManyToManyField('self', through=Follow, symmetrical=False, related_name='following')

    def follow(self, user):
        if not self.is_following(user):
            Follow.objects.create(user_from=self, user_to=user)

    def unfollow(self, user):
        Follow.objects.filter(user_from=self, user_to=user).delete()

    def is_following(self, user):
        return Follow.objects.filter(user_from=self, user_to=user).exists()

    def is_followed_by(self, user):
        return Follow.objects.filter(user_from=user, user_to=self).exists()
