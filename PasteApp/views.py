from django.shortcuts import render
from PasteApp.models import CodePost
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import redirect

class CodePostListView(ListView):
    model = CodePost
    ordering = ['-pub_date']

def home_page(request):
    return render (request, 'PasteApp/Home-Page.html')

def add_paste(request):
    return render (request, 'PasteApp/add_paste.html')

def on_add_paste(request):
    paste = CodePost(title = request.POST['title'], pub_date=timezone.now(), post_content = request.POST['paste'])
    paste.save()
    print(paste.id)
    return redirect ('PasteApp:pasteid', paste_id =paste.id)

def pasteid(request, paste_id):
    paste = CodePost.objects.get(pk=paste_id)
    return render (request, 'PasteApp/paste-id.html', {'paste': paste})

def delete_paste(request, paste_id):
    print(paste_id)
    paste = CodePost.objects.get(pk=paste_id)
    paste.delete()
    return redirect ('PasteApp:list')