from django.db import models
from django.utils.timezone import now


class Player(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    num_stps = models.PositiveIntegerField(default=0)
    stps_date = models.DateField(default=now)
    percentage = models.PositiveIntegerField(default=0)
    predicted_stps = models.PositiveIntegerField(default=0)

    def get_absolute_url():
        return reverse('iipinmotion:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + self.last_name + str(self.num_stps)


class PlayerPlays(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    num_stps = models.PositiveIntegerField(default=0)
    stps_date = models.DateField(default=now)

    def __str__(self):
        return str(self.player.stps_date)
