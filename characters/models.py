from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=140)
    tweeted_at = models.DateTimeField(null=True)
    tweet_id = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name
