from django.db import models

# Create your models here.
from django.db import models


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=50, default="")
    blog_img_caption = models.CharField(max_length=50, default="")
    blog = models.CharField(max_length=30000000)
    blog_image = models.ImageField(upload_to="doge/blog_image", default="")
    blog_bg = models.ImageField(upload_to="doge/blog_image", default="")

    def __str__(self):
        return self.blog_title

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    desc_type = models.CharField(max_length=25, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.user_name



