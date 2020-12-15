from django.urls import path
from . import views
from photoapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index_employee, name='index-employee'),
    path('upload/', views.upload_employee, name='upload-employee'),
    path('update/<int:employee_id>', views.update_employee),
    path('delete/<int:employee_id>', views.delete_employee)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)