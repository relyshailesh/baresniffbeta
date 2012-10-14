from django.shortcuts import render_to_response, get_object_or_404

# Custom view for 404 error
def my_custom_404_view(request):
    return render_to_response('404.html', {})

# Custom view for 500 error
def my_custom_500_view(request):
    return render_to_response('500.html', {})


    
