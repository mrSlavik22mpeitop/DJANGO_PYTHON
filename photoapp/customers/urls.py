from django.urls import path
from . import views
from photoapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index_customer, name='index-customer'),
    path('upload/', views.upload_customer, name='upload-customer'),
    path('update/<int:customer_id>', views.update_customer),
    path('delete/<int:customer_id>', views.delete_customer)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
