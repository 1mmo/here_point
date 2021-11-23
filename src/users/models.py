from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
            default=True,
            db_index=True,
            verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(
            default=True,
            verbose_name='Получать оповещения о новых местах?'
            )
    
    def __str__(self):
        return self.username


    class Meta(AbstractUser.Meta):
        pass
