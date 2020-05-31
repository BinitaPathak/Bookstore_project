from django.shortcuts import render


def home_page(request):
    data = {
        'sitename': 'KodeBlog Shop'
    }

    return render(request, 'index.html', data)  # The render() function takes the request object as its first argument,
    # a template name as its second argument and
    # a dictionary as its optional third argument.
