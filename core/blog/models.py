from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=100,
                            unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now,
                                   db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-publish']
        db_table = 'post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            # Преобразование кириллических символов в латинские и создание slug
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
