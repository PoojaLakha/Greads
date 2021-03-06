from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.db import models

from .search import BookIndex


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    website = models.CharField(validators=[URLValidator()], max_length=200,
                               blank=True)
    twitter_id = models.CharField(max_length=200, blank=True)
    email_id = models.EmailField(max_length=200, null=True, blank=True)
    # member_since = models.DateField()
    about = models.TextField(max_length=3000, null=True)

    class Meta:
        unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    summary = models.TextField(max_length=3000, blank=True)
    # published_year = models.DateField()
    cover_picture = models.ImageField(upload_to='cover_pic',
                                      blank=True)
    # publisher = models.CharField(max_length=100)
    # no_of_pages = models.IntegerField()

    def __str__(self):
        return self.title

    def indexing(self):
        obj = BookIndex(
            meta={'_id': self.isbn},
            title=self.title
        )
        obj.save()
        return obj.to_dict(include_meta=True)


SHELF_CHOICE = (
    ('none', 'Not added to shelf'),
    ('read', 'Read'),
    ('want to read', 'Want to read'),
    ('currently reading', 'currently reading'),
)


class UserBook(models.Model):
    user_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)
    shelf = models.CharField(max_length=100, choices=SHELF_CHOICE,
                             default='none')
    total_books = models.PositiveIntegerField(default=0)
    modified_on = models.DateField()

    class Meta:
        unique_together = (("user_book", "reader"),)

    def __str__(self):
        return '{0}'.format(self.user_book)
