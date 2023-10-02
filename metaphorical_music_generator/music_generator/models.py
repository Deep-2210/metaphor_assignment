from django.db import models

class MusicPiece(models.Model):
    description = models.TextField()
    music_notes = models.TextField()

