from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

from .models import Article,Comment
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from textblob import TextBlob
# Create your views here.


def index(request):
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


@login_required(login_url= "user:login")
def dashboard(request):
    article = Article.objects.filter(author = request.user)
    context = {
        "articles":article
    }
    return render(request,"dashboard.html",context)

def details(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id = id)
    months = {1:"January",
                  2:"Fabruary",
                  3:"March",
                  4:"April",
                  5:"May",
                  6:"June",
                  7:"July",
                  8:"August",
                  9:"September",
                  10:"October",
                  11:"November",
                  12:"December",}
    month_name = months[article.created_date.month]
    comment = article.comments.all()
   
    context = {
        "article":article,
        "months":month_name,
        "comment":comment
    }

    return render(request,"detail.html",context)

@login_required(login_url= "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    print(request.FILES)

    if form.is_valid():
        article = form.save(commit=False) #* Formumuzu Models.py dosyasindan olusturdugumuzdan sadece save() fonksiyonu ile save edebiliyoruz fakat save fonksiyonu bir article objesi create ediyor ve bunu commit etmeye calisiyor fakat biz bir author_id atamadik bu sebepten hata vermemesi icin commit false ile objeyi olusturuyoruz fakat commit ettirmiyoruz db'ye.
        article.author = request.user
        article.save()
        messages.success(request,"Article is successfully added.")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

@login_required(login_url= "user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance= article)
    if form.is_valid():
        article = form.save(commit=False) #* Formumuzu Models.py dosyasindan olusturdugumuzdan sadece save() fonksiyonu ile save edebiliyoruz fakat save fonksiyonu bir article objesi create ediyor ve bunu commit etmeye calisiyor fakat biz bir author_id atamadik bu sebepten hata vermemesi icin commit false ile objeyi olusturuyoruz fakat commit ettirmiyoruz db'ye.
        article.author = request.user
        article.save()
        messages.success(request,"Article is successfully updated.")
        return redirect("article:dashboard")

    context = {
        "form":form
    }
    return render(request,"update.html",context)

@login_required(login_url= "user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Your Article Was Successfully Deleted.")
    
    return redirect("article:dashboard")

def showArticles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()

    context = {
        "articles":articles
    }
    return render(request,"articles.html",context)

def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.user.username
        comment_content = request.POST.get("comment_content")
        blob = TextBlob(comment_content)
        sentiment_score = blob.sentiment.polarity
        temp_sent = ''
        print(sentiment_score)
        if sentiment_score > 0:
            temp_sent = '1'
        elif sentiment_score < 0:
            temp_sent = '-1'
        else:
            temp_sent = '0'
        
        if comment_author != "" and comment_content != "":
            newComment = Comment(comment_author= comment_author,comment_content=comment_content,comment_station=temp_sent)
            newComment.article = article
            
            newComment.save()
            messages.success(request,"Yorum yaptiginiz icin tesekkurler")
            
        elif comment_author != "" and comment_content == "":
            messages.warning(request,"Bos bir Comment olusturamazsiniz.")
    
        elif comment_author == "" and comment_content != "":
            comment_author = "Anonymous"
            newComment = Comment(comment_author= comment_author,comment_content=comment_content,comment_station=temp_sent)
            newComment.article = article
            newComment.save()
            messages.success(request,"Yorum yaptiginiz icin tesekkurler")
        elif comment_author == "" and comment_content == "":
            messages.warning(request,"Bos bir Comment olusturamazsiniz.")
            
    return redirect(reverse("article:detail",kwargs={"id":id}))
