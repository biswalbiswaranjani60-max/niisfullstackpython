from django.shortcuts import render

def form_view(request):
    return render(request, 'form.html')

def result_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        marks = request.POST.get('marks')

        context = {
            'name': name,
            'roll': roll,
            'marks': marks
        }
        return render(request, 'result.html', context)

    return render(request, 'form.html')