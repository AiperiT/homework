from django.shortcuts import render

# Create your views here.
def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    else:
        first_number = request.POST.get('first_number')
        second_number = request.POST.get('second_number')
        action = request.POST.get('action')
        c = ''

        first_number = int(first_number)
        second_number = int(second_number)
        if action == 'add':
            c = first_number + second_number
            action = '+'
        elif action == 'subtract':
            c = first_number - second_number
            action = '-'
        elif action == 'multiply':
            c = first_number * second_number
            action = '*'
        elif action == 'divide':
            if first_number == 0:
                c = 'number cannot be divided by zero'
                action = '/'
            else:
                c = first_number / second_number
                action = '/'

        context = {
            'first_number': request.POST.get('first_number'),
            'second_number': request.POST.get('second_number'),
            'action': action,
            'result': c
        }

        return render(request, 'main.html', context)