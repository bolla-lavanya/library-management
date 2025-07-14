from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Library

# Create your views here.
def display(request):
    if request.method=='GET':
        return render(request,'library/insert.html')
def insertBook(request):
    if request.method=='GET':
        return render(request,'library/insert.html')
    if request.method=='POST':
        lib_id=int(request.POST['lib_id'])
        author=request.POST['author']
        title=request.POST['title']
        genre=request.POST['genre']
        lobj=Library.objects.create(lib_id=lib_id,author=author,title=title,genre=genre)
        return redirect('selecturl')
def updateBook(request,lno):
    lobj=Library.objects.get(lib_id=lno)
    if request.method=='GET':
        return render(request,'library/update.html',{'lobj':lobj})
    if request.method=='POST':
        author = request.POST.get('author', lobj.author)
        title = request.POST.get('title', lobj.title)
        genre = request.POST.get('genre', lobj.genre)

        lobj.author = author
        lobj.title = title
        lobj.genre = genre
        lobj.save()
        return redirect('selecturl')
def deleteBook(request,eno):
    lobj=Library.objects.get(lib_id=eno)
    if request.method=='GET':
        return render(request,'library/delete.html',{'lobj':lobj})
    if request.method=='POST':
        lobj.delete()
    return redirect('selecturl')
def selectBook(request):
    lobj=Library.objects.all()

    if request.method=='GET':
        return render(request,'library/select.html',{'lobj':lobj})

    
