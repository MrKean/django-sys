from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm  # 假设你已经创建了表单类

from django.db.models import Q
from .forms import FileUploadForm
from .models import UploadedFile

def person_list(request):
    # 查询功能
    search_name = request.GET.get('search_name', '')
    query = Q()

    if search_name:
        query &= Q(name__icontains=search_name)

    persons = Person.objects.filter(query)

    context = {'persons': persons, 'search_name': search_name}

    # 文件上传功能
    if request.method == 'POST':

        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("should have messages")
            uploaded_file = form.save(commit=False)
            uploaded_file.uploader = request.user
            uploaded_file.save()
            messages.success(request, "上传成功！")
            
            context.update({'form': form, 'uploaded_file': uploaded_file})
    else:
        form = FileUploadForm()
        context['form'] = form

    files = UploadedFile.objects.all().order_by('-uploaded_at')
    context['files'] = files

    return render(request, 'curd_sql_demo/person_list.html', context)




def person_create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'curd_sql_demo/person_form.html', {'form': form})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'curd_sql_demo/person_form.html', {'form': form, 'person': person})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'curd_sql_demo/person_confirm_delete.html', {'person': person})


from django.shortcuts import get_object_or_404, redirect, render

from .models import UploadedFile

def delete_file(request, pk):
    uploaded_file = get_object_or_404(UploadedFile, id=pk)
    if request.method == 'POST':
        # 删除文件系统中的文件
        uploaded_file.file.delete(save=False)
        # 删除数据库中的记录
        uploaded_file.delete()
        messages.success(request, "文件记录删除成功！")
        return redirect('person_list')  # 假设这是显示所有上传文件的视图的名称
    else:
        print("not post")
    return redirect('person_list')







