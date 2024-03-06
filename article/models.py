from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) #* Burada auth.User daki User silinirse article daki butun verielr de silenecek
    title =  models.CharField(max_length=50)
    content = CKEditor5Field('Content',config_name='extends',blank=True)
    created_date = models.DateTimeField(auto_now_add=True) #* Eklendigi tarihi otomatik olarak almasini saglayan parametre
    updated_date = models.DateTimeField(auto_now = True)
    article_img = models.FileField(blank=True,null=True,verbose_name="Add Image to your Article.")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "name")
    comment_station = models.CharField(max_length=2,verbose_name="station")
    comment_content = models.CharField(max_length = 200,verbose_name = "Content")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ['-comment_date']