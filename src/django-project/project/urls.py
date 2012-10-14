from django.conf.urls.defaults import *

# Define custom view for 404 error
handler404 = "djangoproject.views.my_custom_404_view"
# Define custom view for 500 error
# handler500 = "djangoproject.views.my_custom_500_view"

import test.urls

urlpatterns = patterns('',
    (r'^api/', include(test.urls)),  
)
