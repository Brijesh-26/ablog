from django.db import models
from django.contrib.auth.models import User


# Create your models here.
    
    
class Post(models.Model):
    title= models.CharField(max_length=100)
    header_image= models.ImageField(null=True, blank=True, upload_to='image/')
    desc= models.TextField(max_length=1000)
    posted_on= models.DateField(auto_now_add=True)
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE)
    likes= models.ManyToManyField(User, related_name='liked_posts')
    
    def __str__(self):
        return str(self.pk)
    
    # def get_absolute_url(self):
    #     return reverse("home", kwargs={"pk": self.id})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    
    


