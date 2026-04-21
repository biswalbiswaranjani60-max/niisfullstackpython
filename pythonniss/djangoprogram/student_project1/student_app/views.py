from django.shortcuts import render
from .models import Student

def student_form(request):
    if request.method == "POST":
        roll = request.POST.get('rollno')
        name = request.POST.get('name')
        marks = request.POST.get('marks')

        Student.objects.create(
            rollno=roll,
            name=name,
            marks=marks
        )

    return render(request, 'form.html')