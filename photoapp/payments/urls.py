from django.urls import path
from . import views
from photoapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index_payment, name='index-payment'),
    path('upload/', views.upload_payment, name='upload-payment'),
    path('update/<int:payment_id>', views.update_payment),
    path('delete/<int:payment_id>', views.delete_payment)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)