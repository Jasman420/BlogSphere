from django.db import models
from django.contrib.auth.models import User

STATUS = [
    ('published', 'Published'),
    ('draft', 'Draft')
]

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    category_description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True 
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title