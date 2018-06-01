from django.db import models
# imports for Post model
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

# define custom model manager to retrieve all posts with published status
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# define Post model (basic model for blog posts)
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Field for post title. CharField translates to a varchar column in the SQL database.
    title = models.CharField(max_length=250)
    # This is a field intended to be used in URLs. A slug is a short label containing 
    # only letters, numbers, underscores or hyphens.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # This field defines a many to one relationship. A user can write several posts.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Body of the text. Translates to a text column in the sql database.
    body = models.TextField()
    # This date time indicates when the post was published.
    publish = models.DateTimeField(default=timezone.now)
    # This data time indicates when the post was created.
    created = models.DateTimeField(auto_now_add=True)
    # This date time indicates the last time the post was updated.
    updated = models.DateTimeField(auto_now=True)
    # Show the status of the post
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager() # the default manager
    published = PublishedManager() # the custom manager

    # contains meta data
    class Meta:
        # descending order is specified by the negative prefix
        ordering = ('-publish',)

    # string method is the human readable representation of the object
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:post_detail', args=[self.publish.year,
                                                self.publish.strftime('%m'),
                                                self.publish.strftime('%d'),
                                                self.slug])