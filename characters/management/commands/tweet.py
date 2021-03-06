import requests
from datetime import datetime
from uuid import uuid4
from django.conf import settings
from django.core.management.base import BaseCommand
from characters.models import Character

class Command(BaseCommand):
    help = "Tweet the next character"

    def handle(self, *args, **kwargs):
        characters = Character.objects.order_by('?').filter(tweeted_at__isnull=True)
        if characters.exists():
            character = characters[0]
            tweet_text = "{} dies.".format(character.name)
            tweet_id = self.tweet(tweet_text)
            character.tweeted_at = datetime.now()
            character.tweet_id = tweet_id
            character.save()
            print "{}: {}".format(tweet_id, tweet_text)

    def tweet(self, tweet_text):
        auth = (settings.FOAUTH_USERNAME, settings.FOAUTH_PASSWORD)
        url = 'https://foauth.org/api.twitter.com/1.1/statuses/update.json'
        response = requests.post(url, data={'status': tweet_text}, auth=auth)
        if response.status_code != 200:
            raise Exception("Tweet failed: {}".format(response.content))
        return response.json()['id_str']
