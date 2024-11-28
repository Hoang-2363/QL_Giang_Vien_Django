from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Khoa
from .forms import KhoaForm


def trangchu(request):
    return render(request, 'trangchu.html')

def index(request):
    return render(request, 'khoa/index.html',{
        'khoa': Khoa.objects.all()
    })

def view_student(request, id):
    student = Khoa.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
  if request.method == 'POST':
    form = KhoaForm(request.POST)
    if form.is_valid():
      new_ma_khoa = form.cleaned_data['ma_khoa']
      new_ten_khoa = form.cleaned_data['ten_khoa']

      new_student = Khoa(
        ma_khoa = new_ma_khoa,
        ten_khoa = new_ten_khoa
      )
      new_student.save()
      return render(request, 'khoa/add.html', {
        'form': KhoaForm(),
        'success': True
      })
  else:
    form = KhoaForm()
  return render(request, 'khoa/add.html', {
    'form': KhoaForm()
  })

def edit(request, id):
    if request.method == 'POST':
        student = Khoa.objects.get(pk=id)
        form = KhoaForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return render(request, 'khoa/edit.html', {
            'form': form,
            'success': True
        })
    else:
        student = Khoa.objects.get(pk=id)
        form = KhoaForm(instance=student)
    return render(request, 'khoa/edit.html', {
        'form': form
})

def delete(request, id):
  if request.method == 'POST':
    student = Khoa.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))