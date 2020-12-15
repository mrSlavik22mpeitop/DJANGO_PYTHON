from django.urls import path
from . import views
from photoapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index_product, name='index-product'),
    path('upload/', views.upload_product, name='upload-product'),
    path('update/<int:product_id>', views.update_product),
    path('delete/<int:product_id>', views.delete_product)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
