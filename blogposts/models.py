from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATEGORY = (
    (0, "Facialcare"),
    (1, "Bodycare"),
    (2, "Selfcare"),
    (3, "Diet & Food")
)

# Create your models here.

class Category(models.Model):
    title = models.IntegerField(choices=CATEGORY, default=2)
    slug = models.SlugField(max_length=100, db_index=True)

class Tag(models.Model):
    hashtag = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogposts')
    published_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=False)


