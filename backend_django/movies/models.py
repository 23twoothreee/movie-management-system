from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster_url = models.URLField(blank=True)
    video_file = models.FileField(upload_to='videos/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title