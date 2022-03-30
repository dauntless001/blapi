from django.db import models
from django.utils.text import slugify
from blapi.utils.choices import PostStatusChoices
from blapi.utils.models import TimeBasedModel
from blapi.utils.image import image_path
from post.managers import PostManager
# Create your models here.


class Post(TimeBasedModel):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=1500)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey('post.Category', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(default=PostStatusChoices.draft, choices=PostStatusChoices.choices, max_length=50)

    objects = PostManager()

    class Meta:
        ordering = ['-created_at']
    
    # def save(self, force_insert=False,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super(Post, self).save(args, kwargs)


    def __str__(self):
        return f'Post {self.title}'


class Image(TimeBasedModel):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='post_image')
    image = models.ImageField(upload_to=image_path)

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return f'{self.post} image {self.id}'


class Category(TimeBasedModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name