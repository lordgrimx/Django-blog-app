from django import forms
from .models import Article
from django_ckeditor_5.widgets import CKEditor5Widget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_img"]
        