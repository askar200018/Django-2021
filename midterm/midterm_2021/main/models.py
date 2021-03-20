from django.db import models
from utils.constants import JOURNAL_TYPES, JOURNAL_TYPE_BULLET


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=80)


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES, default=JOURNAL_TYPE_BULLET)
    publisher = models.CharField(max_length=200)
