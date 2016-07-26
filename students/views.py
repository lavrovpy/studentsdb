# Create your views here.
# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Андрій',
         'last_name': u'Лавренюк',
         'ticket': 666777,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Ярослав',
         'last_name': u'Гуменюк',
         'ticket': 673447,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Колодій',
         'last_name': u'Ігор',
         'ticket': 578744,
         'image': 'img/3.jpg'},
        {'id': 4,
         'first_name': u'Пігуль',
         'last_name': u'Олександр',
         'ticket': 673444,
         'image': 'img/4.jpg'},)
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
