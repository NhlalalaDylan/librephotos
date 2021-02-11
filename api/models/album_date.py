from datetime import datetime
from django.db import models
from django.db.models import Prefetch
import api.util as util
from api.models.photo import Photo
from api.models.user import User, get_deleted_user
from collections import Counter
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.contrib.postgres.fields import JSONField

class AlbumDate(models.Model):
    title = models.CharField(
        blank=True, null=True, max_length=512, db_index=True)
    date = models.DateField(db_index=True, null=True)
    photos = models.ManyToManyField(Photo)
    favorited = models.BooleanField(default=False, db_index=True)
    location = JSONField(blank=True, db_index=True, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.SET(get_deleted_user), default=None)
    shared_to = models.ManyToManyField(
        User, related_name='album_date_shared_to')

    class Meta:
        unique_together = ('date', 'owner')

    def __str__(self):
        return "%d: %s" % (self.id, self.title)

    def ordered_photos(self):
        return self.photos.all().order_by('-exif_timestamp')

def get_or_create_album_date(date, owner):
    return AlbumDate.objects.get_or_create(date=date, owner=owner)[0]

def get_album_date(date, owner):
    try:
        return AlbumDate.objects.get(date=date, owner=owner)
    except:
        return None

def get_album_nodate(owner):
    return AlbumDate.objects.get_or_create(date=None, owner=owner)[0]
