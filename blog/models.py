from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, 
    blank=False, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
    related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=10000, blank=False, 
    null=False, default='Share your story!')
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=500, blank=False, 
    null=False, default='Tell us a little bit about your post!')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', 
    blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name="comments")
    name = models.CharField(max_length=100, default=False)
    email = models.EmailField()
    body = models.TextField(default='Share your opinion!', max_length=500, 
    blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    font_awesome_class = models.CharField(max_length=50, blank=True, null=True)
    # Everything in the url before the user handle
    # e.g. https://instagram.com/ or tiktok.com/@
    base_url = models.CharField(max_length=50, blank=True, null=True, 
    default='https://instagram.com/ or https://tiktok.com/@')

    def __str__(self):
        return self.base_url

# class SocialMediaPage(models.Model):
#    platform = models.ForeignKey(base_url)
#    platform = models.ForeignKey(SocialMediaPlatform.objects.get(self))
    # e.g. barrack.obama
#    handle = models.CharField(max_length=50, blank=True, null=True)
#    last_updated = models.DateTimeField(auto_now=True)