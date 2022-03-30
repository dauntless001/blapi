from django.db import models
from django.utils.text import slugify
from blapi.utils.choices import BlogStatusChoices
from blapi.utils.models import TimeBasedModel
from blapi.utils.image import image_path
from blog.managers import BlogManager
# Create your models here.


class Blog(TimeBasedModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=1500)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    status = models.CharField(default=BlogStatusChoices.draft, choices=BlogStatusChoices.choices, max_length=50)

    objects = BlogManager()

    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(args, kwargs)


    def __str__(self):
        return f'Blog {self.title}'


class BlogImage(TimeBasedModel):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name='blog_image')
    image = models.ImageField(upload_to=image_path)

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return f'{self.blog} image {self.id}'