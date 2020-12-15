from django.urls import path
from . import views
from photoapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index_order, name='index-order'),
    path('upload/', views.upload_order, name='upload-order'),
    path('update/<int:order_id>', views.update_order),
    path('delete/<int:order_id>', views.delete_order)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
