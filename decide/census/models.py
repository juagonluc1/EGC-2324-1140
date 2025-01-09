from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    texto1="Este es el texto para el fallo 1"
    
    class Meta:
        unique_together = (('voting_id', 'voter_id',texto1),)
