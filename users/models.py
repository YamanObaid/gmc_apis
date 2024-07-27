"""from django.contrib.auth.models import User, Group
from django.db import models

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'group')
        db_table = 'users_membership'"""