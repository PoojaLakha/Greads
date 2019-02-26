from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)
    # desciption = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # website = models.CharField(blank=True)
    # twitter_id = models.CharField(blank=True)
    # member_since = models.DateField()
    about = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    summary = models.TextField()
    # published_year = models.DateField()
    # cover_picture = models.ImageField(upload_to='pic_path',
    #                                   default='pic_path_for_default_pic')
    # publisher = models.CharField(max_length=100)
    # no_of_pages = models.IntegerField()

    def __str__(self):
        return self.title


class UserBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)

    BOOK_SHELF = (
        ('n', 'none'),
        ('c', 'Currently reading'),
        ('r', 'Read'),
        ('w', 'want to read'),
    )

    shelf = models.CharField(
        max_length=1,
        choices=BOOK_SHELF,
        blank=False,
        default='n',
        help_text='Book shelf',
    )

    class Meta:
        unique_together = (('book', 'reader'),)

    def __str__(self):
        return '%s %s' % (self.id, self.book.title)
