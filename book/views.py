from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
# Create your views here.


def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/index.html', {'shelf': shelf})
    
def upload(request):
    book = BookForm()
    if request.method == 'POST':
        book = BookForm(request.POST, request.FILES)
        if book.is_valid():
            book.save()
            return redirect('book/index.html')
        else:
            return HttpResponse("""Your form is not valid <a href="{{ url 'book_app:index' }}"> reload</a> """)
    else:
        return HttpResponse(request, 'book/upload.html', {'upload_form': book})

def updated_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('book_app:index')
    book_form = BookForm(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('book_app:index')
    return render(request, 'book_app:upload', {'upload_form':book_form})

def deleted_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('book/index.html')
    book_sel.delete()
    return redirect('book/index.html')


    
